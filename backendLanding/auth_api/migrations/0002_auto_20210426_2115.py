# Generated by Django 3.1.4 on 2021-04-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
