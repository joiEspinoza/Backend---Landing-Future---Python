# Generated by Django 3.1.4 on 2021-04-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_api', '0005_auto_20210427_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='textBody',
            field=models.CharField(max_length=15000),
        ),
    ]
