from django.db import models


class Region(models.Model):
    """Region of announcement"""
    region = models.CharField(max_length=50, verbose_name="Название региона")

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регион"


class City(models.Model):
    """City of announcement"""
    city = models.CharField(max_length=50, verbose_name="Название города")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Регион")

    def __str__(self):
        return self.city


class Registration(models.Model):
    """Registration of car"""
    registration = models.CharField(max_length=50, verbose_name="Учет")

    def __str__(self):
        return self.registration
