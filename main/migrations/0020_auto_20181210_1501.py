# Generated by Django 2.0 on 2018-12-10 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20181210_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 10, 15, 1, 48, 232083)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 10, 15, 1, 48, 232083)),
        ),
        migrations.AlterField(
            model_name='farmland',
            name='full_name',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 10, 15, 1, 48, 234083)),
        ),
    ]
