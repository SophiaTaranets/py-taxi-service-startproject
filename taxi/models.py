from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.



class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name}, {self.country}"



class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f"{self.username} ({self.first_name}, {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['model']

    def __str__(self):
        return f"{self.model}, {self.manufacturer}"



