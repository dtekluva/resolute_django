# Generated by Django 2.0 on 2019-01-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0013_auto_20190108_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='if_farmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='if_herdsman',
            field=models.BooleanField(default=False),
        ),
    ]