# Generated by Django 2.0.7 on 2018-07-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_smtprelay_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='smtprelay',
            name='hostname',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
    ]
