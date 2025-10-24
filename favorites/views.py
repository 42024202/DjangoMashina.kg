from django.shortcuts import render
from .models import Favorite
from django.http import JsonResponse
from auto.models import CarAnnouncement
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


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
def toggle_favorite(request, model_name, object_id):
    content_type = get_object_or_404(ContentType, model=model_name)
    obj = content_type.get_object_for_this_type(id=object_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )

    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'added'})
