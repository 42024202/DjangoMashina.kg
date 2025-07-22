from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .models import CarAnnouncement, CarImage, Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, EngineCapacity, EnginePower, CarCondition, Region, City, BodyType, ColorOfCar, Transmission, Drive, WheelType, Exchange, Registration, CustomClearence, Availability, CarMeleage, Profile
from .forms import CarAnnouncementForm
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    """Главная страница."""
    cars = CarAnnouncement.objects.all()
    return render(request, 'main/index.html', {'cars': cars})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            messages.success(request, 'Вы успешно создали аккаунт')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserCreationForm()
    return render(request, 'main/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Вы вошли в аккаунт.')
                return redirect('index')
            else:
                messages.error(request, 'Неправильные данные для входа.')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')
    return render(request, 'main/login.html')


def logout_view(request):
    if request.method == 'POST':
        django_logout(request)
        messages.success(request, 'Вы вышли из аккаунта.')
    return redirect('index')


def car_detail(request, car_id):
    """Подробнее о машине."""
    car = CarAnnouncement.objects.get(id=car_id)
    return render(request, 'main/car_detail.html', {'car': car,})


def add_announcement(request):
    marks = MarkOfCar.objects.all()
    form = CarAnnouncementForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        announcement = form.save(commit=False)
        profile = Profile.objects.get(user=request.user)
        announcement.profile = profile
        announcement.save()
        for image in request.FILES.getlist('images'):
            CarImage.objects.create(announcement=announcement, image=image)

        return redirect('index')

    return render(request, 'main/add_announcement.html', {'form': form, 'marks': marks})


def get_models(request):
    mark_id = request.GET.get('mark_id')
    models = ModelOfCar.objects.filter(mark_id=mark_id).values('id', 'model_name')
    return JsonResponse(list(models), safe=False)


def category(request, category_name):
    """Категории."""
    category = Category.objects.get(name=category_name)
    cars = CarAnnouncement.objects.filter(category=category)
    mark = request.GET.get('mark')
    model = request.GET.get('model')
    engine_type = request.GET.get('engine_type')

    engine_capacity = request.GET.get('engine_capacity')
    power_from = request.GET.get('power_from')
    power_to = request.GET.get('power_to')
    meleage_from = request.GET.get('meleage_from')
    meleage_to = request.GET.get('meleage_to')

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
    if engine_capacity:
        cars = cars.filter(engine_capacity__engine_capacity=engine_capacity)
    if power_from:
        cars = cars.filter(engine_power__engine_power__gte=power_from)
    if power_to:
        cars = cars.filter(engine_power__engine_power__lte=power_to)
    if meleage_from:
        cars = cars.filter(car_meleage__car_meleage__gte=meleage_from)
    if meleage_to:
        cars = cars.filter(car_meleage__car_meleage__lte=meleage_to)
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
    if is_available == 'on':
        cars = cars.filter(is_available__is_available__icontains=is_available)

    marks = MarkOfCar.objects.all()
    models = ModelOfCar.objects.filter(mark_id=mark) if mark else []
    context = {
        'cars': cars,
        'category': category,
        'marks': marks,
        'models': models,
            }
    return render(request, 'main/category.html', context=context)


def delete_announcement(request, car_id):
    if request.method == 'POST':
        car = get_object_or_404(CarAnnouncement, id=car_id)
        CarImage.objects.filter(announcement=car).delete()
        car.delete()
        return redirect('index')


