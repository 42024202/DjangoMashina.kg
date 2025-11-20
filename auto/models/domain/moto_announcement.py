from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from common.models import Mark, Model, Region, City, Condition, Availability, MotoSeries
from ..shared.characters import Color, Exchange, YearOfProduction, Registration, CustomClearence
from django.utils.text import slugify
from django.urls import reverse

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

    slug = models.SlugField(
            max_length=50,
            blank=True,
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

    series = models.ForeignKey(
            MotoSeries,
            on_delete=models.PROTECT,
            verbose_name="Серия"
            )

    year_of_production = models.ForeignKey(
            YearOfProduction,
            on_delete=models.PROTECT,
            verbose_name="Год выпуска"
            )

    car_mileage = models.PositiveIntegerField(
            verbose_name="Пробег (км)"
            )

    color = models.ForeignKey(
            Color,
            on_delete=models.PROTECT,
            verbose_name="Цвет",
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=2,
            verbose_name="Цена ($)"
            )

    condition = models.ForeignKey(
            Condition,
            on_delete=models.PROTECT,
            verbose_name="Состояние"
            )

    availability = models.ForeignKey(
            Availability,
            on_delete=models.PROTECT,
            verbose_name="Доступность"
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

    exchange = models.ForeignKey(
            Exchange,
            on_delete=models.PROTECT,
            verbose_name="Обмен"
            )

    registration = models.ForeignKey(
            Registration,
            on_delete=models.PROTECT,
            verbose_name="Регистрация"
            )

    custom_clearence = models.ForeignKey(
            CustomClearence,
            on_delete=models.PROTECT,
            verbose_name="Растаможка"
            )

    urgency = models.BooleanField(
            default=False,
            verbose_name="Срочно"
            )

    description = models.TextField(
            verbose_name="Описание",
            blank=True,
            null=True
            )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating and not self.slug:
            base_slug = slugify(f"{self.mark}-{self.model}-{self.series}")
            self.slug = base_slug
            super().save(update_fields=["slug"])
       
    def __str__(self):
        return f"{self.mark} {self.model} {self.series}"

    def get_absolute_url(self):
        return reverse("auto:moto_detail", kwargs={"moto_id": self.id, "moto_slug": self.slug})


    class Meta:

        verbose_name = "Объявление о мототранспорте"
        verbose_name_plural = "Объявления о мототранспорте"

        ordering = ["-created_at"]


class MotoAnnouncementImage(models.Model):  
        moto_announcement = models.ForeignKey(
                MotoAnnouncement,
                on_delete=models.CASCADE,
                related_name="images",
                verbose_name="Объявление о мототранспорте"
                )
        
        image = models.ImageField(
                upload_to="moto_announcements/",
                verbose_name="Изображение",
                )

