from django.db import models
from ..domain.announcement import CarAnnouncement


class CarImage(models.Model):
    announcement = models.ForeignKey(
            CarAnnouncement,
            on_delete=models.CASCADE,
            related_name='images',
            )

    image = models.ImageField(
            upload_to="car_images",
            verbose_name="Фото"
            )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

