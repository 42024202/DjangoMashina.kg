from django.db import models 
from accounts.models import CustomUser
from common.models import (
        Mark, Model, Generation,
        Region, City, Condition, Availability
        )


class CarForPart:
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name='Профиль'
            )

    name = models.CharField(
            max_length=30,
            verbose_name='Название'
            )

    mark = models.ForeignKey(
            Mark,
            models.PROTECT,
            verbose_name='Марка'
            )

    model = models.ForeignKey(
            Model,
            models.PROTECT,
            verbose_name='Модель'
            )

    generation = models.ForeignKey(
            Generation,
            models.PROTECT,
            verbose_name='Поколение'
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=1,
            verbose_name='Цена'
            )

    region = models.ForeignKey(
            Region,
            models.PROTECT,
            verbose_name='Регион'
            )

    city = models.ForeignKey(
            City,
            models.PROTECT,
            verbose_name='Город'
            )

    condition = models.ForeignKey(
            Condition,
            models.PROTECT,
            verbose_name='Состояние'
            )

    availability = models.ForeignKey(
            Availability,
            models.PROTECT,
            verbose_name='Доступность'
            )

    description = models.TextField(
            verbose_name='Описание'
            )
    
    def __str__(self):
        return f"{self.name} {self.mark} {self.model}"

    class Meta:
        verbose_name = "Машина на запчасти"
        verbose_name_plural = "Машины на запчасти"


class CarForPartImage(models.Model):
    car_for_parts = models.ForeignKey(
            CarForPart,
            models.CASCADE,
            verbose_name='Машина на запчасти'
            )
    image = models.ImageField(
            verbose_name='Фото'
            )

    def __str__(self):
        return f"{self.car_for_parts.name}"

    class Meta:
        verbose_name = "Фотография машины на запчасти"
        verbose_name_plural = "Фотографии машин на запчасти"

