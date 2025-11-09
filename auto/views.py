from django.contrib.auth.models import ContentType
from django.db import transaction 
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import CarAnnouncement, CarImage, Category
from .models.car_configs.car_config import CarConfig
from .filters import CarAnnouncementFilter
from favorites.models import Favorite
from .forms import CarAnnouncementForm, CarConfigForm, CarImageForm
from .services.multi_form_mixin import MultiFormCreateView, MulriFormUpdateView
from django.core.exceptions import PermissionDenied


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
        user = self.request.user
        context['is_favorite'] = (
                self.request.user.is_authenticated and
                Favorite.objects.filter(
                    user=user,
                    content_type=ContentType.objects.get_for_model(car),
                    object_id=car.id).exists()
                )
        context['app_label'] = car._meta.app_label
        context['model_name'] = car._meta.model_name
        context['is_owner'] = user.is_authenticated and user == car.profile
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
        #context['categories'] = Category.objects.all(parent__isnull=True)
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


class UpdateAnnouncementView(LoginRequiredMixin, MulriFormUpdateView):
    model = CarAnnouncement
    template_name = 'auto/create_announcement.html'
    pk_url_kwarg = 'car_id'
    success_url = reverse_lazy('auto:get_my_announcements')
    form_class = CarAnnouncementForm
    form_classes = {
            'announcement': CarAnnouncementForm,
            'config': CarConfigForm,
            'images': CarImageForm
            }
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile != self.request.user:
            raise PermissionDenied("Вы не можете редактировать это объявление.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updating'] = True
        return context


class DeleteAnnouncementView(LoginRequiredMixin, DeleteView):
    model = CarAnnouncement
    template_name = 'auto/delete_confirmation.html'
    success_url = reverse_lazy('auto:get_my_announcements')
    pk_url_kwarg = 'car_id'

    def get(self, request, *args, **kwargs):
        print("DEBUG: DeleteAnnouncementView GET вызван")
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile != self.request.user:
            raise PermissionDenied("Вы не можете удалить это объявление.")
        return obj

