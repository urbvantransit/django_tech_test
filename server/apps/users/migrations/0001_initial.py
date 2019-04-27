# Generated by Django 2.1.2 on 2019-04-26 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='permissions', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('option', models.CharField(choices=[('A', 'Administrador'), ('D', 'Conductor'), ('U', 'Usuario')], default='U', max_length=1)),
            ],
        ),
    ]