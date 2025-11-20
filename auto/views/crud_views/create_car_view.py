from django.shortcuts import render, redirect
from django.db import transaction 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from auto.models import CarAnnouncement, CarImage
from auto.models.car_configs.car_config import CarConfig
from auto.filters import CarAnnouncementFilter
from auto.forms import CarAnnouncementForm, CarConfigForm, CarImageForm
from auto.services.multi_form_mixin import MultiFormCreateView


class CreateCarAnnouncementView(LoginRequiredMixin, MultiFormCreateView):
    model = CarAnnouncement
    template_name = 'auto/create_announcement.html'
    success_url = reverse_lazy('favorites:get_my_announcements')
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

