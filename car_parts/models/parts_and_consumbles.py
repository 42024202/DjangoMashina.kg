from django.db import models 
from accounts.models import CustomUser
from common.models import (
        Mark, Model, Generation,
        Region, City, Condition, Availability
        )


class PartsAndConsumble(models.Model):
    profile = models.ForeignKey(
            CustomUser,
            models.CASCADE,
            related_name='parts_and_consumbles',
            verbose_name='Профиль'
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
            blank=True,
            null=True,
            verbose_name='Описание'
            )
    def __str__(self):
        return f"Запчасти на {self.mark} {self.model} {self.generation}"
    
    class Meta:
        verbose_name = 'Запчасти и расходники'
        verbose_name_plural = 'Запчасти и расходники'
        ordering = ['-id']


class PartsAndConsumblesImage(models.Model):
    parts_and_consumbles = models.ForeignKey(
            PartsAndConsumble,
            on_delete=models.CASCADE,
            related_name='images',
            verbose_name='Запчасти и расходники'
            )
    images = models.ImageField(
                upload_to="parts_and_consumbles_images/",
                verbose_name="Фото запчастей и расходников"
                )
    def __str__(self):
        return f"Фотографии"

    class Meta:
        verbose_name = 'Фотография запчасти и расходника'
        verbose_name_plural = 'Фотографии запчастей и расходников'

