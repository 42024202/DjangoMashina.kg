from django.db import models
from accounts.models import CustomUser
from common.models import (
        Mark, Model, Generation,
        Region, City, Condition, Availability
        )


class CarOil(models.Model):
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name="Профиль"
            )

    name = models.CharField(
            max_length=30,
            verbose_name="Название"
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
            verbose_name="Поколение"
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=1,
            verbose_name="Цена"
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

    description = models.TextField(
            verbose_name="Описание"
            )

    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name="Дата создания"
            )

    updated_at = models.DateTimeField(
            auto_now=True,
            verbose_name="Дата изменения"
            )
    
    def __str__(self):
        return f"{self.name} {self.mark} {self.model}"

    class Meta:
        verbose_name = "Масло и химия"
        verbose_name_plural = "Масла и химия"
        ordering = ["-id"]



class CarOilsImage(models.Model):
    car_oils = models.ForeignKey(
            CarOil,
            on_delete=models.CASCADE,
            verbose_name="Масло и химия"
            )

    image = models.ImageField(
            verbose_name="Фото",
            upload_to="car_oils/"
            )

    def __str__(self):
        return f"{self.car_oils.name}"

    class Meta:
        verbose_name = "Фото масла и химии"
        verbose_name_plural = "Фото масел и химий"

