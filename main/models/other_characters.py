from django.db import models


class Availability(models.Model):
    availability = models.CharField(max_length=100, blank=True, null=True, verbose_name="Доступность")

    def __str__(self):
        return self.availability


    class Meta:
        verbose_name = "Доступность"
        verbose_name_plural = "Доступность"


class Exchange(models.Model):
    exchange = models.CharField(max_length=100, blank=True, null=True, verbose_name="Обмен")

    def __str__(self):
        return self.exchange


    class Meta:
        verbose_name = "Обмен"
        verbose_name_plural = "Обмен"


class CustomClearence(models.Model):
    """CustomClearence of car."""
    custom_clearence = models.CharField(max_length=100, blank=True, null=True, verbose_name="Растаможка")

    def __str__(self):
        return self.custom_clearence


    class Meta:
        verbose_name = "Растаможка"
        verbose_name_plural = "Растаможка"
