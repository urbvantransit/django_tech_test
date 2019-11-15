# Generated by Django 2.1.2 on 2019-11-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20191114_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationmodel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='locationmodel',
            name='longitude',
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='coordinates',
            field=models.CharField(default='', max_length=100),
        ),
    ]
