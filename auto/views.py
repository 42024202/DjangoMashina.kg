from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import CarAnnouncement
from django.utils import timezone
from .filters import CarAnnouncenmentFilter
from django.contrib.contenttypes.models import ContentType
from favorites.models import Favorite


def index(request):
    """Главная страница."""
    cars = CarAnnouncement.objects.all()
    car_ct = ContentType.objects.get_for_model(CarAnnouncement)
    if request.GET.get('urgent') == '1':
        cars = CarAnnouncement.objects.filter(urgency=True)
    return render(
            request, 
            'auto/index.html', 
            context={
                'cars': cars,
                }
            )
    

def car_detail(request, car_id):
    car = get_object_or_404(CarAnnouncement, id=car_id)
    is_fav = False
    if request.user.is_authenticated:
        is_fav = Favorite.is_favorite(request.user, car) 
    return render(
            request, 
            'auto/car_detail.html', 
            context={
                'car': car,
                'is_favorite': is_fav
             }
            )


def category_view(request, category_name):
    car_list = CarAnnouncement.objects.filter(category__name=category_name)
    car_filter = CarAnnouncenmentFilter(request.GET, queryset=car_list)
    return render(
        request,
        'auto/category.html',
        {
            'filter': car_filter,
            'cars': car_filter.qs,
            'category_name': category_name,
        }
    )


