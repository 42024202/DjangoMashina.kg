from django.views.generic.edit import UpdateView
from django.core.exceptions import ImproperlyConfigured
from typing import Type
from django.db.models import Model


class ImageFormMixin(UpdateView):
    announcement_image_model: Type[Model] | None = None
    image_fk_name: str = "announcement"

    def form_valid(self, form):
        if not self.announcement_image_model:
            raise ImproperlyConfigured("announcement_image_model is not set")

        response = super().form_valid(form)

        delete_ids = self.request.POST.getlist('delete_images')
        if delete_ids:
            self.announcement_image_model.objects.filter(
                id__in=delete_ids,
                **{self.image_fk_name: self.object}
            ).delete()

        images = self.request.FILES.getlist('images')
        for image in images:
            self.announcement_image_model.objects.create(
                **{self.image_fk_name: self.object},
                image=image
            )

        return response

