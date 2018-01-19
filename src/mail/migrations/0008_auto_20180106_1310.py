# Generated by Django 2.0 on 2018-01-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_auto_20180101_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='mailq_id',
            field=models.TextField(default='', verbose_name='Mailqueue identification'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='blacklisted',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='client_ip',
            field=models.GenericIPAddressField(db_index=True, verbose_name='Client IP'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_address',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_domain',
            field=models.CharField(blank=True, db_index=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='message',
            name='infected',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_rbl_listed',
            field=models.BooleanField(db_index=True, verbose_name='Is RBL listed'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_spam',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='mailscanner_hostname',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='quarantined',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='spam_score',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_address',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255, verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_domain',
            field=models.CharField(blank=True, db_index=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='message',
            name='whitelisted',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'from_domain'], name='mail_messag_from_ad_73cd6c_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'to_domain'], name='mail_messag_to_addr_0cd3ce_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'to_address'], name='mail_messag_from_ad_f1acb9_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'to_domain'], name='mail_messag_from_ad_5833fe_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'from_domain'], name='mail_messag_to_addr_06c9aa_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'mailscanner_hostname'], name='mail_messag_client__f7ba93_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'blacklisted'], name='mail_messag_from_ad_676957_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'whitelisted'], name='mail_messag_from_ad_238390_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'infected'], name='mail_messag_from_ad_1f0d67_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'is_spam'], name='mail_messag_from_ad_12e43e_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'quarantined'], name='mail_messag_from_ad_2d4929_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_address', 'is_rbl_listed'], name='mail_messag_from_ad_2b9f87_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'blacklisted'], name='mail_messag_to_addr_eec52d_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'whitelisted'], name='mail_messag_to_addr_0f2921_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'infected'], name='mail_messag_to_addr_a7125d_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'is_spam'], name='mail_messag_to_addr_5cae52_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'quarantined'], name='mail_messag_to_addr_11d06f_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_address', 'is_rbl_listed'], name='mail_messag_to_addr_1e8598_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'blacklisted'], name='mail_messag_from_do_bf466c_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'whitelisted'], name='mail_messag_from_do_be122b_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'infected'], name='mail_messag_from_do_4a62bf_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'is_spam'], name='mail_messag_from_do_3d2668_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'quarantined'], name='mail_messag_from_do_e2e93e_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['from_domain', 'is_rbl_listed'], name='mail_messag_from_do_d8e7ed_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'blacklisted'], name='mail_messag_to_doma_48b624_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'whitelisted'], name='mail_messag_to_doma_da63ed_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'infected'], name='mail_messag_to_doma_e640e6_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'is_spam'], name='mail_messag_to_doma_752e4f_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'quarantined'], name='mail_messag_to_doma_1647b6_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['to_domain', 'is_rbl_listed'], name='mail_messag_to_doma_729d90_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'blacklisted'], name='mail_messag_client__31eae6_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'whitelisted'], name='mail_messag_client__9d8977_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'infected'], name='mail_messag_client__1577f4_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'is_spam'], name='mail_messag_client__ef32e1_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'quarantined'], name='mail_messag_client__0c4c11_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['client_ip', 'is_rbl_listed'], name='mail_messag_client__961a40_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'blacklisted'], name='mail_messag_mailsca_eec5db_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'whitelisted'], name='mail_messag_mailsca_e7750e_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'infected'], name='mail_messag_mailsca_9bc8e2_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'is_spam'], name='mail_messag_mailsca_04192b_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'quarantined'], name='mail_messag_mailsca_75aba8_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['mailscanner_hostname', 'is_rbl_listed'], name='mail_messag_mailsca_7437e6_idx'),
        ),
    ]