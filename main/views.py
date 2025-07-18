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


def category(request, category_name):
    """Категории."""
    category = Category.objects.get(name=category_name)
    cars = Car.objects.filter(category=category)
    mark = request.GET.get('mark')
    model = request.GET.get('model')
    engine_type = request.GET.get('engine_type')
    body_type = request.GET.get('body_type')
    region = request.GET.get('region')
    color = request.GET.get('color')
    car_condition = request.GET.get('car_condition')
    year = request.GET.get('year')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')

    if mark:
        cars = cars.filter(mark__mark_name__icontains=mark)
    if model:
        cars = cars.filter(model__icontains=model)
    if engine_type:
        cars = cars.filter(engine_type__icontains=engine_type)
    if body_type:
        cars = cars.filter(body_type__icontains=body_type)
    if region:
        cars = cars.filter(region__icontains=region)
    if color:
        cars = cars.filter(color__icontains=color)
    if car_condition:
        cars = cars.filter(car_condition__icontains=car_condition)
    if year:
        cars = cars.filter(year=year)
    if price_from:
        cars = cars.filter(price__gte=price_from)
    if price_to:
        cars = cars.filter(price__lte=price_to)
    context = {
        'cars': cars,
        'category': category
            }
    return render(request, 'main/category.html', context=context)
