# Generated by Django 2.1.2 on 2019-07-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='id',
            field=models.CharField(default='loc_201971019471248d9c8b8', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.CharField(default='sta_201971019471231403075', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
