from django.db import models
from .category import Category, MarkOfCar, ModelOfCar
from .characters import EngineType, EngineCapacity, EnginePower, BodyType, Drive, WheelType, Transmission
from .region import Region, City, Registration
from .car_condition import YearOfProduction, ColorOfCar, CarMeleage, CarCondition
from .other_characters import Availability, Exchange, CustomClearence


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")


class Car_announcement(models.Model):
    """Anouncement on web-site."""
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория", related_name="cars_by_categories")

    mark = models.ForeignKey(MarkOfCar, on_delete=models.PROTECT, null=True, verbose_name="Марка", related_name="cars_by_marks")

    model = models.ForeignKey(ModelOfCar, on_delete=models.PROTECT, null=True, verbose_name="Модель", related_name="cars_by_models")

    year = models.ForeignKey(YearOfProduction, on_delete=models.PROTECT, null=True, verbose_name="Год выпуска", related_name="cars_by_years") 
    
    price = models.ForeignKey(Price, on_delete=models.PROTECT, null=True, verbose_name="Цена", related_name="cars_by_prices")

    engine = models.ForeignKey(EngineType, on_delete=models.PROTECT, null=True, verbose_name="Двигатель", related_name="cars_by_engines")

    engine_capacity = models.ForeignKey(EngineCapacity, on_delete=models.PROTECT, verbose_name="Объем двигателя", related_name="cars_by_engine_capacities")

    engine_power = models.ForeignKey(EnginePower, on_delete=models.PROTECT, verbose_name="Мощность двигателя", related_name="cars_by_engine_powers")

    car_meleage = models.ForeignKey(CarMeleage, on_delete=models.PROTECT, verbose_name="Пробег", related_name="cars_by_meleages")

    car_condition = models.ForeignKey(CarCondition, on_delete=models.PROTECT, null=True, verbose_name="Состояние", related_query_name="cars_by_conditions", blank=True)

    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, verbose_name="Регион", related_name="cars_by_regions", blank=True)

    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name="Город", related_name="cars_by_cities", blank=True)

    body = models.ForeignKey(BodyType, on_delete=models.PROTECT, null=True, verbose_name="Кузов", related_name="cars_by_bodies")

    color = models.ForeignKey(ColorOfCar, on_delete=models.PROTECT, null=True, verbose_name="Цвет", related_name="colors", blank=True)

    transmission = models.ForeignKey(Transmission, on_delete=models.PROTECT, null=True, verbose_name="Тип коробки", related_name="cars_by_transmissions", blank=True)

    drive = models.ForeignKey(Drive, on_delete=models.PROTECT, null=True, verbose_name="Привод", related_name="cars_by_drives", blank=True)

    wheel_type = models.ForeignKey(WheelType, on_delete=models.PROTECT, null=True, verbose_name="Руль", related_name="cars_by_wheel_types", blank=True)

    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT, null=True, verbose_name="Обмен", related_name="cars_by_exchanges", blank=True)

    registration = models.ForeignKey(Registration, on_delete=models.PROTECT, null=True, verbose_name="Учет", related_name="cars_by_registrations", blank=True)

    custom_clearence = models.ForeignKey(CustomClearence, on_delete=models.PROTECT, null=True, verbose_name="Растаможка", related_name="cars_by_customs", blank=True)

    description = models.TextField(verbose_name="Описание")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_available = models.ForeignKey(Availability, on_delete=models.PROTECT, null=True, verbose_name="Доступность", related_name="cars_by_availability")

    urgency_of_announcement = models.BooleanField()

class CarImage(models.Model):
    announcement = models.ForeignKey(Car_announcement, on_delete=models.PROTECT, verbose_name="Фотографии")
    images = models.ImageField(upload_to='cars_images/', verbose_name="Изображение")
