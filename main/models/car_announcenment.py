from django.db import models
from django.db.models.deletion import PROTECT
from .characters import( 
    Exchange, Category, Color, WheelType, 
    YearOfProduction, Registration, CustomClearence,
    )
from .car_config import CarConfig
from django.utils import timezone
from datetime import timedelta
import uuid


class CarAnnouncement(models.Model):
    profile = models.ForeignKey(
            "accounts.CustomUser", 
            on_delete=models.PROTECT, 
            verbose_name="Профиль", 
            related_name="announcements"
            )

    category = models.ForeignKey(
            Category, 
            on_delete=models.PROTECT, 
            verbose_name="Категория", 
            related_name="announcements_by_category"
            )

    car_config = models.ForeignKey(
            CarConfig, 
            on_delete=models.PROTECT, 
            verbose_name="Конфигурация"
            )

    color = models.ForeignKey(
            Color,
            on_delete=models.PROTECT,
            verbose_name="Цвет автомобиля"
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=1, 
            verbose_name="Цена"
            )

    engine_power = models.DecimalField(
            decimal_places=2,
            max_digits=4,
            verbose_name="Мощность двигателя"
            )

    car_mileage = models.PositiveBigIntegerField(
            verbose_name="Пробег"
            )

    wheel_type = models.ForeignKey(
            WheelType, 
            on_delete=models.PROTECT, 
            verbose_name="Тип руля"
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
            verbose_name="Состояние"
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
            verbose_name="Дата обновления"
            )

    urgency = models.CharField(
            max_length=30,
            verbose_name="Срочность объявления"
            )

    year = models.ForeignKey(
            YearOfProduction, 
            on_delete=models.PROTECT, 
            verbose_name="Год выпуска"
            )

    region = models.ForeignKey(
            "common.Region", 
            on_delete=models.PROTECT, 
            verbose_name="Регион"
            )

    city = models.ForeignKey(
            "common.City", 
            on_delete=models.PROTECT, 
            verbose_name="Город"
            )

    car_condition = models.ForeignKey(
            "common.Condition",
            on_delete=models.PROTECT,
            verbose_name="Состояние машины"
            )

    availability = models.ForeignKey(
            "common.Avalability",
            on_delete=models.PROTECT,
            verbose_name="Доступность"
            )

    def get_active_promotion(self):
        """Find active promotion for car_announcement to now"""
        return self.promotions.filter(end_date__gt=timezone.now()).order_by('-end_date').first()

    def is_premium(self):
        """Check does it relate to premium promotion"""
        promotion = self.get_active_promotion()
        return promotion and promotion.tariff.tariff_type == 'premium'

    def is_vip(self):
        """Check does it relate to vip promotion"""
        promotion = self.get_active_promotion()
        return promotion and promotion.tariff.tariff_type == 'vip'
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class CarImage(models.Model):
    announcement = models.ForeignKey(
            CarAnnouncement,
            on_delete=models.CASCADE,
            related_name='images',
            )

    image = models.ImageField(
            upload_to="car_images",
            verbose_name="Фото"
            )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Tariff(models.Model):
    """Tariffes for users"""
    TARIFF_TYPES = (
        ('premium', 'Премиум'),
        ('vip', 'Вип'),
            )

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

