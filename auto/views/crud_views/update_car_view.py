from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from auto.models import CarAnnouncement, CarImage
from auto.forms import CarAnnouncementForm, CarConfigForm, CarImageForm
from auto.services.multi_form_mixin import MulriFormUpdateView
from auto.services.image_form_mixin import ImageFormMixin
from django.core.exceptions import PermissionDenied


class UpdateCarAnnouncementView(LoginRequiredMixin, ImageFormMixin, MulriFormUpdateView):
    model = CarAnnouncement
    template_name = 'auto/create_announcement.html'
    pk_url_kwarg = 'car_id'
    success_url = reverse_lazy('favorites:get_my_announcements')
    form_class = CarAnnouncementForm
    form_classes = {
            'announcement': CarAnnouncementForm,
            'config': CarConfigForm,
            'images': CarImageForm
            }

    announcement_image_model = CarImage
    image_fk_name = "announcement"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile != self.request.user:
            raise PermissionDenied("Вы не можете редактировать это объявление.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not hasattr(self, 'forms'):
            self.forms = self.get_forms()

        context['forms'] = self.forms
        context['form'] = self.forms['announcement']
        context['images'] = CarImage.objects.filter(announcement=self.object)
        context['updating'] = True

        return context

    def forms_valid(self, forms):
        response = super().forms_valid(forms)

        delete_ids = self.request.POST.getlist("delete_images")

        for img_id in delete_ids:
            img = CarImage.objects.filter(id=img_id, announcement=self.object).first()
            if img:
                img.image.delete(save=False)
                img.delete()

        for file in self.request.FILES.getlist("images"):
            CarImage.objects.create(announcement=self.object, image=file)

        return response
