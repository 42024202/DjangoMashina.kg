from django.shortcuts import render, redirect
from .models import Car_announcement, CarImage, Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, EngineCapacity, EnginePower, CarCondition, Region, City, BodyType, ColorOfCar, Transmission, Drive, WheelType, Exchange, Registration, CustomClearence, Availability, CarMeleage


def index(request):
    """Главная страница."""
    cars = Car_announcement.objects.all()
    return render(request, 'main/index.html', {'cars': cars})


def car_detail(request, car_id):
    """Подробнее о машине."""
    car = Car_announcement.objects.get(id=car_id)
    return render(request, 'main/car_detail.html', {'car': car})


def add_car(request):
    if request.method == 'POST':
        try:
            car = Car_announcement.objects.create(
                category_id=request.POST.get('category'),
                mark_id=request.POST.get('mark'),
                model_id=request.POST.get('model'),
                year_id=request.POST.get('year'),
                price=request.POST.get('price'),
                engine_id=request.POST.get('engine'),
                car_condition_id=request.POST.get('car_condition'),
                region_id=request.POST.get('region'),
                city_id=request.POST.get('city'),
                body_id=request.POST.get('body'),
                color_id=request.POST.get('color'),
                transmission_id=request.POST.get('transmission'),
                drive_id=request.POST.get('drive'),
                wheel_type_id=request.POST.get('wheel_type'),
                exchange_id=request.POST.get('exchange'),
                registration_id=request.POST.get('registration'),
                custom_clearence_id=request.POST.get('custom_clearence'),
                description=request.POST.get('description'),
                is_available_id=request.POST.get('is_available'),
                is_quickly_id=request.POST.get('is_quickly'),
            )

            for img in request.FILES.getlist('images'):
                CarImage.objects.create(car=car, image=img)

            return redirect('index')
        except Exception as e:
            print("Ошибка при сохранении:", e)
            context = {'error': str(e)}

    else:
        context = {}

    context.update({
        'categories': Category.objects.all(),
        'marks': MarkOfCar.objects.all(),
        'models': ModelOfCar.objects.all(),
        'years': YearOfProduction.objects.all(),
        'engines': EngineType.objects.all(),
        'car_conditions': CarCondition.objects.all(),
        'regions': Region.objects.all(),
        'cities': City.objects.all(),
        'bodies': BodyType.objects.all(),
        'colors': ColorOfCar.objects.all(),
        'transmissions': Transmission.objects.all(),
        'drives': Drive.objects.all(),
        'wheel_types': WheelType.objects.all(),
        'exchanges': Exchange.objects.all(),
        'registrations': Registration.objects.all(),
        'custom_clearences': CustomClearence.objects.all(),
        'availabilities': Availability.objects.all(),
    })
    return render(request, 'main/add_announcement.html', context)


def category(request, category_name):
    """Категории."""
    category = Category.objects.get(name=category_name)
    cars = Car_announcement.objects.filter(category=category)
    mark = request.GET.get('mark')
    model = request.GET.get('model')
    engine_type = request.GET.get('engine_type')
    body = request.GET.get('body')
    region = request.GET.get('region')
    color = request.GET.get('color')
    car_condition = request.GET.get('car_condition')
    year = request.GET.get('year')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')

    city = request.GET.get('city')
    drive = request.GET.get('drive')
    wheel_type = request.GET.get('wheel_type')
    exchange = request.GET.get('exchange')
    registration = request.GET.get('registration')
    is_available = request.GET.get('is_available')

    if mark:
        cars = cars.filter(mark__mark_name__icontains=mark)
    if model:
        cars = cars.filter(model__model_name__icontains=model)
    if engine_type:
        cars = cars.filter(engine__engine__icontains=engine_type)

    if body:
        cars = cars.filter(body__body__icontains=body)
    if region:
        cars = cars.filter(region__region__icontains=region)
    if color:
        cars = cars.filter(color__color__icontains=color)
    if car_condition:
        cars = cars.filter(car_condition__car_condition__icontains=car_condition)
    if year:
        cars = cars.filter(year__year=year)
    if price_from:
        cars = cars.filter(price__gte=price_from)
    if price_to:
        cars = cars.filter(price__lte=price_to)
    if drive:
        cars = cars.filter(drive__drive__icontains=drive)
    if city:
        cars = cars.filter(city__city__icontains=city)
    if wheel_type:
        cars = cars.filter(wheel_type__wheel_type__icontains=wheel_type)
    if exchange:
        cars = cars.filter(exchange__exchange__icontains=exchange)
    if registration:
        cars = cars.filter(registration__registration__icontains=registration)
    if is_available:
        cars = cars.filter(is_available__is_available__icontains=is_available)
    context = {
        'cars': cars,
        'category': category
            }
    return render(request, 'main/category.html', context=context)


def add_announcement(request):
    return render(request, 'main/add_announcement.html')
