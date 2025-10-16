from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import CarAnnouncement, CarImage
from .filters import CarAnnouncementFilter
from favorites.models import Favorite
from django.contrib.auth.decorators import login_required
from .forms import CarAnnouncementForm, CarConfigForm, CarImageForm


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


class CreateAnnouncementView(LoginRequiredMixin, CreateView):
    template_name = 'auto/create_announcement.html'
    success_url = reverse_lazy('auto:get_my_announcements')
    form_class = CarAnnouncementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config_form'] = context.get('config_form', CarConfigForm())
        context['image_form'] = context.get('image_form', CarImageForm())
        return context

    def post(self, request, *args, **kwargs):
        config_form = CarConfigForm(request.POST)
        announcement_form = CarAnnouncementForm(request.POST)
        image_form = CarImageForm(request.POST, request.FILES)

        if config_form.is_valid() and announcement_form.is_valid():
            car_config = config_form.save()
            car_announcement = announcement_form.save(commit=False)
            car_announcement.car_config = car_config
            car_announcement.profile = request.user
            car_announcement.save()

            for img in request.FILES.getlist('image'):
                CarImage.objects.create(announcement=car_announcement, image=img)

            return redirect(self.success_url)

        return self.render_to_response({
            'config_form': config_form,
            'form': announcement_form,
            'image_form': image_form,
        })

