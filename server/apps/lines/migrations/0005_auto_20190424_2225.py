# Generated by Django 2.1.2 on 2019-04-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0004_auto_20190424_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_20194242225437a8941c5', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_2019424222543a63235a8', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
