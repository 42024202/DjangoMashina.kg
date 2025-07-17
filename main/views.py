from django.shortcuts import render
from .models import Category, Car


def index(request):
    """Главная страница."""
    cars = Car.objects.all()
    return render(request, 'main/index.html', {'cars': cars})


def car_detail(request, car_id):
    """Подробнее о машине."""
    car = Car.objects.get(id=car_id)
    return render(request, 'main/car_detail.html', {'car': car})


def passenger_cars(request):
    """Легковые автомобили."""
    cars = Car.objects.filter(category__name='Легковые')
    return render(request, 'main/passenger_cars.html', {'cars': cars})


def moto_cars(request):
    """Мотоциклы."""
    cars = Car.objects.filter(category__name='Мото')
    return render(request, 'main/moto.html', {'cars': cars})


def commercial_cars(request):
    """Коммерческие автомобили."""
    cars = Car.objects.filter(category__name='Коммерческие')
    return render(request, 'main/commercial.html', {'cars': cars})
