from django.shortcuts import render
from .models import Favorite
from django.http import JsonResponse
from main.models import CarAnnouncement
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType


@login_required
def favorites_announcenments_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    cars = [fav.content_object for fav in favorites]
    return render(
            request,
            'favorites/favorites.html',
            {'cars': cars}
            )


@login_required
def toggle_favorite(request, car_id):
    """Add anouncement to favorites"""
    car = CarAnnouncement.objects.get(id=car_id)
    content_type = ContentType.objects.get_for_model(CarAnnouncement)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=car.id
    )

    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'added'})

