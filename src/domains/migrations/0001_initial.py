# Generated by Django 2.0.5 on 2018-05-15 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('destination', models.CharField(blank=True, max_length=128, null=True)),
                ('relay_type', models.CharField(default='smtp', max_length=64)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('catchall', models.BooleanField(default=False)),
                ('allowed_accounts', models.IntegerField(default=-1)),
            ],
        ),
    ]
