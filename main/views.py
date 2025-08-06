from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import CarAnnouncement
from django.utils import timezone
from .filters import CarAnnouncenmentFilter


def index(request):
    """Главная страница."""
    cars = CarAnnouncement.objects.all()
    return render(
            request, 
            'main/index.html', 
            {'cars': cars}
            )

def car_detail(request, car_id):
    car = get_object_or_404(CarAnnouncement, id=car_id)
    return render(
            request, 
            'main/car_detail.html', 
            {'car': car}
            )

def category_view(request, category_name):
    car_list = CarAnnouncement.objects.filter(category__name=category_name)
    car_filter = CarAnnouncenmentFilter(request.GET, queryset=car_list)
    return render(
        request,
        'main/category.html',
        {
            'filter': car_filter,
            'cars': car_filter.qs,
            'category_name': category_name
        }
    )

