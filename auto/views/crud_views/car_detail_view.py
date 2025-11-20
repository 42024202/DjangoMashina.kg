from django.contrib.auth.models import ContentType
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from auto.models import CarAnnouncement
from favorites.models import Favorite


class CarDetailView(DetailView):
    """Detail view for car announcement"""
    model = CarAnnouncement
    template_name = 'auto/car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    slug_url_kwarg = 'car_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(
            CarAnnouncement,
            id=self.kwargs['car_id'],
            slug=self.kwargs['car_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        user = self.request.user
        context['is_favorite'] = (
                self.request.user.is_authenticated and
                Favorite.objects.filter(
                    user=user,
                    content_type=ContentType.objects.get_for_model(car),
                    object_id=car.id).exists()
                )
        context['app_label'] = car._meta.app_label
        context['model_name'] = car._meta.object_name
        context['is_owner'] = user.is_authenticated and user == car.profile
        return context

