from django.db import models
from django.contrib.auth import get_user_model
from common.models import Mark, Model, Region, City, Condition, Availability, Generation


User = get_user_model()


class TypeOfMotorcycle(models.Model):
    name = models.CharField(
            max_length=50,
            verbose_name="Название"
            )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Тип мототранспорта"
        verbose_name_plural = "Типы мототранспортов"


class MotoAnnouncement(models.Model):
    profile = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            verbose_name="Профиль"
            )

    type_of_moto = models.ForeignKey(
            TypeOfMotorcycle,
            on_delete=models.PROTECT,
            verbose_name="Тип мототранспорта"
            )

    mark = models.ForeignKey(
            Mark,
            on_delete=models.PROTECT,
            verbose_name="Марка"
            )

    model = models.ForeignKey(
            Model,
            on_delete=models.PROTECT,
            verbose_name="Модель"
            )

    generation = models.ForeignKey(
            Generation,
            on_delete=models.PROTECT,
            verbose_name="Серия"
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=2,
            verbose_name="Цена (сом)"
            )

    region = models.ForeignKey(
            Region,
            on_delete=models.PROTECT,
            verbose_name="Регион"
            )

    city = models.ForeignKey(
            City,
            on_delete=models.PROTECT,
            verbose_name="Город"
            )

    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mark} {self.model} {self.generation}"


    class Meta:

        verbose_name = "Объявление о мототранспорте"
        verbose_name_plural = "Объявления о мототранспорте"

        ordering = ["-created_at"]


class MotoAnnouncementImage(models.Model):  
        moto_announcement = models.ForeignKey(
                MotoAnnouncement,
                on_delete=models.CASCADE,
                verbose_name="Объявление о мототранспорте"
                )
        
        image = models.ImageField(
                upload_to="moto_announcements/",
                verbose_name="Изображение"
                )

