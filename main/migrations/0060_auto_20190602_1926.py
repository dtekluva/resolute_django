# Generated by Django 2.0 on 2019-06-02 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_auto_20190602_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positions',
            options={},
        ),
        migrations.AlterField(
            model_name='collection',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 19, 26, 28, 64669)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 19, 26, 28, 64669)),
        ),
        migrations.AlterField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 2, 19, 26, 28, 80292)),
        ),
    ]