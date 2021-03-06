# Generated by Django 3.1.1 on 2020-11-09 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
                ('fname', models.CharField(default='', max_length=50)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('economy_vacancy', models.PositiveIntegerField(default=0)),
                ('economy_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('business_vacancy', models.PositiveIntegerField(default=0)),
                ('business_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.CharField(default='Delhi', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.CreateModel(
            name='Hotel_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.customer')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Flight_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.customer')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.flight')),
            ],
        ),
    ]
