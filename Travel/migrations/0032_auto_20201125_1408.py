# Generated by Django 3.1.1 on 2020-11-25 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0031_auto_20201124_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_booking',
            name='customer',
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='user_email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='user_fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='user_lname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 25, 14, 8, 4, 101765)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 25, 14, 8, 4, 101765)),
        ),
    ]