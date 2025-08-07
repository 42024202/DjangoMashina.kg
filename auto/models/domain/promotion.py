from common.choices import TARIFF_TYPES
from django.db import models
from ..domain.announcement import CarAnnouncement
from django.utils import timezone
from datetime import timedelta
import uuid


class Tariff(models.Model):
    """Tariffes for users"""
    
    name = models.CharField(
            max_length=50, 
            choices=TARIFF_TYPES, 
            verbose_name='Тип тарифа'
            )

    price = models.DecimalField(
            max_digits=10, 
            decimal_places=2, 
            verbose_name='Цена (сом)'
            )

    duration_days = models.PositiveIntegerField(
            verbose_name='Срок действия (в днях)'
            )

    def __str__(self):
        return f"{self.get_name_display()} — {self.price} сом / {self.duration_days} дн."

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class Promotion(models.Model):
    """Promotion for car_announcenments"""
    car_announcement = models.ForeignKey(
            CarAnnouncement, 
            on_delete=models.CASCADE, 
            related_name='promotions'
            )

    tariff = models.ForeignKey(
            Tariff, 
            on_delete=models.CASCADE, 
            verbose_name='Тариф'
            )

    start_date = models.DateTimeField(
            default=timezone.now, 
            verbose_name='Начало действия'
            )

    end_date = models.DateTimeField(
            blank=True,
            null=True, 
            verbose_name='Конец действия'
            )

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.tariff.duration_days)
        super().save(*args, **kwargs)

    def is_active(self):
        return self.start_date <= timezone.now() <= self.end_date

    def __str__(self):
        return f"{self.tariff} для {self.car_announcement}"

    class Meta:
        verbose_name = "Продвижение"
        verbose_name_plural = "Продвижения"

