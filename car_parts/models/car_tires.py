from django.db import models
from accounts.models import CustomUser
from common.models import (
        Mark, Model, Generation,
        Region, City, Condition, Availability
        )


class TireType(models.Model):
    tire_type = models.CharField(
            max_length=30,
            verbose_name='Тип шин'
            )


class CarTire(models.Model):
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name='Профиль'
            )

    car_tire_type = models.ForeignKey(
            TireType,
            on_delete=models.PROTECT,
            verbose_name='Тип шин'
            )

    tire_width = models.PositiveSmallIntegerField(
            verbose_name='Ширина шин'
            )

    tire_height = models.DecimalField(
            max_digits=4,
            decimal_places=1,
            verbose_name='Высота шин'
            )

    tire_size = models.CharField(
            max_length=30,
            verbose_name='Размер шин'
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=1,
            verbose_name='Цена'
            )

    mark = models.ForeignKey(
            Mark,
            on_delete=models.PROTECT,
            verbose_name='Марка'
            )

    model = models.ForeignKey(
            Model,
            on_delete=models.PROTECT,
            verbose_name='Модель'
            )

    generation = models.ForeignKey(
            Generation,
            on_delete=models.PROTECT,
            verbose_name='Поколение'
            )
    
    def str(self):
        return f"{self.car_tire_type}  {self.tire_size}"

    class Meta:
        verbose_name = 'Шина'
        verbose_name_plural = 'Шины'
        
        ordering = ['-id']


class CarTireImage(models.Model):
    car_tire = models.ForeignKey(
            CarTire,
            on_delete=models.CASCADE,
            verbose_name='Шины'
            )

    image = models.FileField(
            upload_to='media/',
            verbose_name='Фото'
            )

    verbose_name = 'Фото шин'
    verbose_name_plural = 'Фото шин'
