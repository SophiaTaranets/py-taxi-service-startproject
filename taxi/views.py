from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request):
    # обрпховуємо кількість екземплярів моделей
    driver_number = Driver.objects.count()
    car_number = Car.objects.count()
    man_number = Manufacturer.objects.count()
    context ={
        "driver_number": driver_number,
        "car_number": car_number,
        "man_number": man_number
    }
    return render(request, "taxi/index.html", context=context)
