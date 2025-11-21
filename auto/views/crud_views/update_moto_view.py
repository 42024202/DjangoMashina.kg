from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from auto.models import MotoAnnouncement, MotoAnnouncementImage
from auto.forms import MotoAnnouncementForm
from django.core.exceptions import PermissionDenied


class UpdateMotoAnnouncementView(LoginRequiredMixin, UpdateView):
    model = MotoAnnouncement
    form_class = MotoAnnouncementForm
    template_name = 'auto/create_announcement.html'
    pk_url_kwarg = 'moto_id'
    success_url = reverse_lazy('favorites:get_my_announcements')

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

    def form_valid(self, form):
        response = super().form_valid(form)

        """Delete old images, which marked with user"""
        delete_images = self.request.POST.getlist('delete_images')
        if delete_images:
            MotoAnnouncementImage.objects.filter(id__in=delete_images).delete()

        images = self.request.FILES.getlist('images')
        for image in images:
            MotoAnnouncementImage.objects.create(
                    moto_announcement=self.object,
                    image=image
                    )

        return response

