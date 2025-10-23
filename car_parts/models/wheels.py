from django.db import models
from accounts.models import CustomUser
from common.models import (
        Mark, Model, Generation,
        Region, City, Condition, Availability
        )


class DiskType(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name="Тип диска"
            )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип диска"
        verbose_name_plural = "Типы дисков"


class DiskWidth(models.Model):
    width = models.PositiveSmallIntegerField(
            verbose_name="Ширина дисков"
            )

    def __str__(self):
        return f"{self.width} мм"

    class Meta:
        verbose_name = "Ширина диска"
        verbose_name_plural = "Ширины дисков"


class DiskHeight(models.Model):
    height = models.DecimalField(
            max_digits=4,
            decimal_places=1,
            verbose_name="Высота дисков"
            )

    def __str__(self):
        return f"{self.height} мм"

    class Meta:
        verbose_name = "Высота диска"
        verbose_name_plural = "Высота дисков"


class DiskDiameter(models.Model):
    diameter = models.DecimalField(
            max_digits=4,
            decimal_places=1,
            verbose_name="Диаметр дисков"
            )
    
    def __str__(self):
        return f"{self.diameter} мм"

    class Meta:
        verbose_name = "Диаметр диска"
        verbose_name_plural = "Диаметры дисков"


class CarDisk(models.Model):
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name="Профиль"
            )

    disk_type = models.ForeignKey(
            DiskType,
            on_delete=models.PROTECT,
            verbose_name="Тип диска"
            )

    disk_width = models.ForeignKey(
            DiskWidth,
            on_delete=models.PROTECT,
            verbose_name="Ширина диска"
            )

    disk_height = models.ForeignKey(
            DiskHeight,
            on_delete=models.PROTECT,
            verbose_name="Высота диска"
            )

    disk_diameter = models.ForeignKey(
            DiskDiameter,
            on_delete=models.PROTECT,
            verbose_name="Диаметр диска"
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

    year_of_production = models.PositiveSmallIntegerField(
            verbose_name="Год выпуска",
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
    
    def __str__(self):
        return f"Диски {self.mark} {self.model} {self.generation}"

    class Meta:
        verbose_name = "Диск"
        verbose_name_plural = "Диски"


class WheelImage(models.Model):
    disk = models.ForeignKey(
            CarDisk,
            on_delete=models.CASCADE,
            verbose_name="Диск"
            )

    image = models.ImageField(
            upload_to='wheels/',
            verbose_name="Изображение"

