# Generated by Django 2.0.7 on 2018-07-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_smtprelay'),
    ]

    operations = [
        migrations.AddField(
            model_name='smtprelay',
            name='active',
            field=models.BooleanField(default=0),
        ),
    ]