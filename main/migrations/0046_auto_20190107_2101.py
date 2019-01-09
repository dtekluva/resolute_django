# Generated by Django 2.0 on 2019-01-07 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20181217_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmland',
            name='lat',
            field=models.FloatField(blank=True, default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='farmland',
            name='lng',
            field=models.FloatField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 7, 21, 1, 9, 160836)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 7, 21, 1, 9, 160836)),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 7, 21, 1, 9, 161832)),
        ),
    ]