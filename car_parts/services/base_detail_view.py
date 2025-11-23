from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from favorites.models import Favorite


class BaseAnnouncementDetailView(DetailView):
    """ Base detail view for car_parts announcements"""

    pk_url_kwarg = "pk"
    context_object_name = "car"

    id_field = "id"

    def get_object(self, queryset=None):
        lookup = {
            self.id_field: self.kwargs.get(self.pk_url_kwarg),
            }
        return get_object_or_404(self.model, **lookup)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        user = self.request.user

        context["is_favorite"] = (
            user.is_authenticated
            and Favorite.objects.filter(
                user=user,
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id,
            ).exists()
        )

        context["is_owner"] = user.is_authenticated and user == obj.profile

        context["app_label"] = obj._meta.app_label
        context["model_name"] = obj._meta.model_name

        return context

