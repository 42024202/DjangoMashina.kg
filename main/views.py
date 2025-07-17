from django.shortcuts import render
from .models import Category, Car


def index(request):
    """Главная страница."""
    cars = Car.objects.all()
    return render(request, 'main/index.html', {'cars': cars})
