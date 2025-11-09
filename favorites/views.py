from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions.math import Log
from django.views.generic import View, ListView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from .models import Favorite 


class ToggleFavoriteView(LoginRequiredMixin, View):
    """Button for adding any type announcement to favorites"""

    def post(self, request, app_label, model_name, object_id):
        content_type = get_object_or_404(ContentType, app_label=app_label, model=model_name)
        obj = content_type.get_object_for_this_type(id=object_id)
        
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj.id
        )

        if not created:
            favorite.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class FavoriteListView(LoginRequiredMixin, ListView):
    """displaying all favorite announcements"""
    model = Favorite
    template_name = 'favorites/favorites.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related('content_type')
    
