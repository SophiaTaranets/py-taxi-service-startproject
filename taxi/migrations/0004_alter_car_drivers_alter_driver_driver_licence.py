# Generated by Django 4.2 on 2023-04-04 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_alter_car_options_alter_car_drivers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_licence',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
