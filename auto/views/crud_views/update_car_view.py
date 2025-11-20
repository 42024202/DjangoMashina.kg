from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from auto.models import CarAnnouncement
from auto.forms import CarAnnouncementForm, CarConfigForm, CarImageForm
from auto.services.multi_form_mixin import MulriFormUpdateView
from django.core.exceptions import PermissionDenied


class UpdateCarAnnouncementView(LoginRequiredMixin, MulriFormUpdateView):
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

