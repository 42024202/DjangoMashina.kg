from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from auto.models import CarAnnouncement
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
    

class MyAnnouncementsView(LoginRequiredMixin, ListView):
    template_name = 'favorites/my_announcements.html'
    context_object_name = 'my_cars'

    def get_queryset(self):
        return CarAnnouncement.objects.filter(profile=self.request.user)


def get_announcement_create(request):
    """Show which form to use for creating an announcement."""
    context = {}
    return render(request, 'auto/choise_template_for_create.html', context)


