# Generated by Django 3.1.4 on 2021-04-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0003_auto_20210427_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
