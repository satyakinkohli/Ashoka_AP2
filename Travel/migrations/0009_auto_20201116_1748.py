# Generated by Django 3.1.3 on 2020-11-16 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0008_auto_20201113_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='number',
            field=models.PositiveSmallIntegerField(default=9999999900),
        ),
        migrations.AddField(
            model_name='hotel',
            name='website',
            field=models.URLField(default='www..com', max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 16, 17, 48, 22, 857033)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 16, 17, 48, 22, 856991)),
        ),
    ]