# Generated by Django 2.0 on 2018-01-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0009_auto_20180109_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='client_ip',
            field=models.GenericIPAddressField(db_index=True, null=True, verbose_name='Client IP'),
        ),
    ]