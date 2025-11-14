from django.db import models
from ..shared.characters import (
    Exchange, Category,
    Color, WheelType, 
    YearOfProduction, Registration, CustomClearence,
            )
from ..car_configs.car_config import CarConfig
from django.utils import timezone
from django.utils.text import slugify


class CarAnnouncement(models.Model):
    profile = models.ForeignKey(
            "accounts.CustomUser", 
            on_delete=models.PROTECT, 
            verbose_name="Профиль", 
            related_name="announcements"
            )
    
    slug = models.SlugField(
            max_length=50,
            blank=True,
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
            decimal_places=1,
            max_digits=9,
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
            verbose_name="Растаможка"
            )

    description = models.TextField(
            verbose_name="Описание",
            blank=True,
            null=True
            )

    created_at = models.DateTimeField(
            auto_now_add=True, 
            verbose_name="Дата создания"
            )

    updated_at = models.DateTimeField(
            auto_now=True, 
            verbose_name="Дата обновления"
            )

    urgency = models.BooleanField(
            default=False, 
            verbose_name="Срочно"
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
            "common.Availability",
            on_delete=models.PROTECT,
            verbose_name="Доступность"
            )

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating and not self.slug:
            base_slug = slugify(f"{self.car_config.mark}-{self.car_config.model}")
            self.slug = f"{base_slug}-{self.pk}"
            super().save(update_fields=["slug"])

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("auto:car_detail", kwargs={"car_id": self.id, "car_slug": self.slug})

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

        ordering = ["-created_at"]

