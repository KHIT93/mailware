#
# MailGuardian for MailScanner
# Copyright (C) 2003-2011  Steve Freegard (steve@freegard.name)
# Copyright (C) 2011  Garrod Alwood (garrod.alwood@lorodoes.com)
# Copyright (C) 2014-2017  MailWatch Team (https://github.com/MailWatch/1.2.0/graphs/contributors)
# Copyright (C) 2018 @KHIT93 (https://github.com/khit93/mailguardian/contributers.md)
#
#   Custom Module SQLSpamSettings
#
#   Version 1.0
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# In addition, as a special exception, the copyright holder gives permission to link the code of this program with
# those files in the PEAR library that are licensed under the PHP License (or with modified versions of those files
# that use the same license as those files), and distribute linked combinations including the two.
# You must obey the GNU General Public License in all respects for all of the code used other than those files in the
# PEAR library that are licensed under the PHP License. If you modify this program, you may extend this exception to
# your version of the program, but you are not obligated to do so.
# If you do not wish to do so, delete this exception statement from your version.
#
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

#
# This module uses entries in the user table to determine the Spam Settings
# for each user.
#

package MailScanner::CustomConfig;

use strict 'vars';
use strict 'refs';
no  strict 'subs'; # Allow bare words for parameter %'s

use vars qw($VERSION);

### The package version, both in 1.23 style *and* usable by MakeMaker:
$VERSION = substr q$Revision: 1.0 $, 10;

use DBI;
my ($dbh);
my ($sth);
my (%LowSpamScores, %HighSpamScores);
my (%ScanList);
my ($sstime, $hstime, $nstime);

# Get database information from MailGuardianConf.pm
use File::Basename;
my $dirname = dirname(__FILE__);
require $dirname.'/MailGuardianConf.pm';

my ($db_name) = MailGuardian_get_db_name();
my ($db_host) = MailGuardian_get_db_host();
my ($db_user) = MailGuardian_get_db_user();
my ($db_pass) = MailGuardian_get_db_password();
my ($ss_score) = 5;       # Define a high default spam score, so that we do not accidently mark mail as spam when something is wrong
my ($ss_high_score) = 15;  # Define a high default high spam score, so that we do not accidently mark mail as hig spam when something is wrong
my ($ss_scan) = 1;          # Make sure that we always scan mail, so that users are still protected when the database is offline

# Get refresh time from from MailGuardianConf.pm
my ($ss_refresh_time) =  MailGuardian_get_SS_refresh_time();

#
# Initialise the arrays with the users Spam settings
#
sub InitSQLSpamScores
{
    my ($entries) = CreateScoreList('custom_spam_score', \%LowSpamScores);
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Read %d Spam entries", $entries);
    $sstime = time();
}

sub InitSQLHighSpamScores
{
    my $entries = CreateScoreList('custom_spam_highscore', \%HighSpamScores);
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Read %d high Spam entries", $entries);
    $hstime = time();
}

sub InitSQLNoScan
{
    my $entries = CreateNoScanList('skip_scan', \%ScanList);
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Read %d No Spam Scan entries", $entries);
    $nstime = time();
}

#
# Lookup a users Spam settings
#
sub SQLSpamScores
{
    # Do we need to refresh the data?
    if ((time() - $sstime) >= ($ss_refresh_time * 60)) {
        MailScanner::Log::InfoLog("MailGuardian: SQLSpamScores refresh time reached");
        InitSQLSpamScores();
    }
    my ($message) = @_;
    my ($score) = LookupScoreList($message, \%LowSpamScores);
    return $score;
}

sub SQLHighSpamScores
{
    # Do we need to refresh the data?
    if ((time() - $hstime) >= ($ss_refresh_time * 60)) {
        MailScanner::Log::InfoLog("MailGuardian: SQLHighSpamScores refresh time reached");
        InitSQLHighSpamScores();
    }
    my ($message) = @_;
    my ($score) = LookupScoreList($message, \%HighSpamScores);
    return $score;
}

sub SQLNoScan
{
    # Do we need to refresh the data?
    if ((time() - $nstime) >= ($ss_refresh_time * 60)) {
        MailScanner::Log::InfoLog("MailGuardian: SQLNoScan refresh time reached");
        InitSQLNoScan();
    }
    my ($message) = @_;
    my ($noscan) = LookupNoScanList($message, \%ScanList);
    return $noscan;
}

sub SQLDefaultScore
{
    my ($sql);

    $dbh = DBI->connect("DBI:Pg:database=$db_name;host=$db_host",
        $db_user, $db_pass,
        { PrintError => 0, AutoCommit => 1, RaiseError => 1 }
    );
    if (!$dbh) {
        MailScanner::Log::WarnLog("MailGuardian: SQLSpamSettings:: CreateScoreList::: Unable to initialise database connection: %s", $DBI::errstr);
    }

    $sql = "SELECT value FROM core_settings WHERE key='mail.spamassassin.score'";
    $sth = $dbh->prepare($sql);
    $sth->execute;
    $sth->bind_columns(undef, \$ss_score);
    $sql = "SELECT value FROM core_settings WHERE key='mail.spamassassin.highscore'";
    $sth = $dbh->prepare($sql);
    $sth->execute;
    $sth->bind_columns(undef, \$ss_high_score);

    # Close connections
    $sth->finish();
    $dbh->disconnect();
}

#
# Close down Spam Settings lists
#
sub EndSQLSpamScores
{
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Closing down MailGuardian SQL Spam Scores");
}

sub EndSQLHighSpamScores
{
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Closing down MailGuardian SQL High Spam Scores");
}

sub EndSQLNoScan
{
    MailScanner::Log::InfoLog("MailGuardian: SQLSpamSettings:: Closing down MailGuardian SQL No Scan");
}

# Read the list of users that have defined their own Spam Score value. Also
# read the domain defaults and the system defaults (defined by the admin user).
sub CreateScoreList
{
    SQLDefaultScore();
    my ($type, $UserList) = @_;
    my ($sql, $username, $count);

    $dbh = DBI->connect("DBI:Pg:database=$db_name;host=$db_host",
        $db_user, $db_pass,
        { PrintError => 0, AutoCommit => 1, RaiseError => 1 }
    );
    if (!$dbh) {
        MailScanner::Log::WarnLog("MailGuardian: SQLSpamSettings:: CreateScoreList::: Unable to initialise database connection: %s", $DBI::errstr);
    }

    $sql = "SELECT email AS username, $type FROM core_user WHERE $type > 0";
    $sth = $dbh->prepare($sql);
    $sth->execute;
    $sth->bind_columns(undef, \$username, \$type);
    $count = 0;
    
    while($sth->fetch())
    {
        $UserList->{lc($username)} = $type; # Store entry
        $count++;
    }

    # Close connections
    $sth->finish();
    $dbh->disconnect();

    return $count;
}

# Read the list of users that have defined that don't want Spam scanning.
sub CreateNoScanList
{
    my ($type, $NoScanList) = @_;
    my ($sql, $username, $count);

    $dbh = DBI->connect("DBI:Pg:database=$db_name;host=$db_host",
        $db_user, $db_pass,
        { PrintError => 0, AutoCommit => 1, RaiseError => 1 }
    );
    if (!$dbh) {
        MailScanner::Log::WarnLog("MailGuardian: SQLSpamSettings::CreateNoScanList::: Unable to initialise database connection: %s", $DBI::errstr);
    }

    $sql = "SELECT email AS username, $type FROM core_user WHERE $type = true";
    $sth = $dbh->prepare($sql);
    $sth->execute;
    $sth->bind_columns(undef, \$username, \$type);
    $count = 0;
    while($sth->fetch())
    {
        $NoScanList->{lc($username)} = 1; # Store entry
        $count++;
    }

    # Close connections
    $sth->finish();
    $dbh->disconnect();

    return $count;
}

# Based on the address it is going to, choose the correct Spam score.
# If the actual "To:" user is not found, then use the domain defaults
# as supplied by the domain administrator. If there is no domain default
# then fallback to the system default as defined in the "admin" user.
# If the user has not supplied a value and the domain administrator has
# not supplied a value and the system administrator has not supplied a
# value, then return 999 which will effectively let everything through
# and nothing will be considered Spam.
#
sub LookupScoreList
{
    my ($message, $LowHigh) = @_;

    return 0 unless $message; # Sanity check the input

    # Find the first "to" address and the "to domain"
    my (@todomain, $todomain, @to, $to);
    @todomain = @{$message->{todomain}};
    $todomain = $todomain[0];
    @to = @{$message->{to}};
    $to = $to[0];

    # It is in the list with the exact address? if not found, get the domain,
    # if that's not found,  get the system default otherwise return a high
    # value to just let the email through.
    return $LowHigh->{$to} if $LowHigh->{$to};
    return $LowHigh->{$todomain} if $LowHigh->{$todomain};

    # There are no Spam scores to return for the given account, so we use the default system values.
    return $ss_score if $ss_score;
    # There are no Spam scores to return if we made it this far, so let the email through.
    return 999;
}

# Based on the address it is going to, decide whether or not to scan.
# the users email for Spam.
sub LookupNoScanList
{
    my ($message, $NoScan) = @_;

    return 0 unless $message; # Sanity check the input

    # Find the first "to" address and the "to domain"
    my (@todomain, $todomain, @to, $to);
    @todomain = @{$message->{todomain}};
    $todomain = $todomain[0];
    @to = @{$message->{to}};
    $to = $to[0];

    # It is in the list with the exact address? if not found, get the domain,
    # if that's not found, return 0
    return 0 if $NoScan->{$to};
    return 0 if $NoScan->{$todomain};

    # There is no setting, then go ahead and scan for Spam, be on the safe side.
    return 1;
}

1;