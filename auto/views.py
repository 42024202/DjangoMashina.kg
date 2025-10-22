from django.db import transaction 
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import CarAnnouncement, CarImage
from .models.car_configs.car_config import CarConfig
from .filters import CarAnnouncementFilter
from favorites.models import Favorite
from .forms import CarAnnouncementForm, CarConfigForm, CarImageForm
from .services.multi_form_mixin import MultiFormCreateView


class IndexView(ListView):
    model = CarAnnouncement
    template_name = 'auto/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('urgent') == '1':
            queryset = queryset.filter(urgency=True)
        return queryset


class CarDetailView(DetailView):
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
        context['is_favorite'] = (
            self.request.user.is_authenticated
            and Favorite.is_favorite(self.request.user, car)
        )
        return context


class CategoryView(ListView):
    template_name = 'auto/category.html'
    context_object_name = 'cars'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        queryset = CarAnnouncement.objects.filter(category__name=category_name)
        self.car_filter = CarAnnouncementFilter(self.request.GET, queryset=queryset)
        return self.car_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.car_filter
        context['category_name'] = self.kwargs['category_name']
        return context


class MyAnnouncementsView(LoginRequiredMixin, ListView):
    template_name = 'auto/my_announcements.html'
    context_object_name = 'my_cars'

    def get_queryset(self):
        return CarAnnouncement.objects.filter(profile=self.request.user)


class CreateAnnouncementView(LoginRequiredMixin, MultiFormCreateView):
    model = CarAnnouncement
    template_name = 'auto/create_announcement.html'
    success_url = reverse_lazy('auto:get_my_announcements')
    form_class = CarAnnouncementForm
    form_classes = {
            'announcement': CarAnnouncementForm,
            'config': CarConfigForm,
            'images': CarImageForm
            }

    def get_context_data(self, **kwargs):
        if not hasattr(self, 'object'):
            self.object = None

        context = super().get_context_data(**kwargs)
        return context

    def forms_valid(self, forms):
        announcement_form = forms['announcement']
        config_form = forms['config']
        config_data = config_form.cleaned_data
        car_config, created = CarConfig.objects.get_or_create(
            mark = config_data['mark'],
            model = config_data['model'],
            generation = config_data['generation'],
            body = config_data['body'],
            engine_type = config_data['engine_type'],
            engine_capacity = config_data['engine_capacity'],
            transmission = config_data['transmission'],
            drive = config_data['drive'],
            defaults = config_data
            )   
        with transaction.atomic():
            car_announcement = announcement_form.save(commit=False)
            car_announcement.car_config = car_config
            car_announcement.profile = self.request.user
            car_announcement.save()

            self.object = car_announcement

            for img in self.request.FILES.getlist('images'):
                CarImage.objects.create(announcement=car_announcement, image=img)
        return redirect(self.success_url)


