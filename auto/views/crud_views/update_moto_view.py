from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from auto.models import MotoAnnouncement, MotoAnnouncementImage
from auto.forms import MotoAnnouncementForm
from django.core.exceptions import PermissionDenied
from auto.services.image_form_mixin import ImageFormMixin

class UpdateMotoAnnouncementView(LoginRequiredMixin, ImageFormMixin, UpdateView):
    model = MotoAnnouncement
    form_class = MotoAnnouncementForm
    template_name = 'auto/create_announcement.html'
    pk_url_kwarg = 'moto_id'
    success_url = reverse_lazy('favorites:get_my_announcements')

    announcement_image_model = MotoAnnouncementImage
    image_fk_name = "moto_announcement"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile != self.request.user:
            raise PermissionDenied("Вы не можете редактировать это объявление.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updating'] = True
        context['images'] = MotoAnnouncementImage.objects.filter(moto_announcement=self.object)
        return context

