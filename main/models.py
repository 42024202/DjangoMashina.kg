from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class MarkOfCar(models.Model):
    """Марка машины."""
    mark_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Марка")

    def __str__(self):
        return self.mark_name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class ModelOfCar(models.Model):
    """Модель машины."""
    mark = models.ForeignKey(MarkOfCar, on_delete=models.CASCADE, verbose_name="Марка")
    model_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Модель")

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
    

class EngineType(models.Model):
    """Тип двигателя."""
    engine = models.CharField(max_length=100, blank=True, null=True, verbose_name="Двигатель")

    class Meta:
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"

    def __str__(self):
        return self.engine


class YearOfProduction(models.Model):
    """Год выпуска."""
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")

    class Meta:
        verbose_name = "Год выпуска"
        verbose_name_plural = "Год выпуска"

    def __str__(self):
        return f"{self.year} г."


class CarCondition(models.Model):
    """Состояние машины."""
    car_condition = models.CharField(max_length=100, blank=True, null=True, verbose_name="Состояние")
    
    class Meta:
        verbose_name = "Состояние"
        verbose_name_plural = "Состояния"

    def __str__(self):
        return self.car_condition


class Region(models.Model):
    """Регион."""
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name="Регион")

    def __str__(self):
        return self.region
    
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class City(models.Model):
    """Город."""
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")

    def __str__(self):
        return self.city


class BodyType(models.Model):
    """Тип кузова."""
    body = models.CharField(max_length=100, blank=True, null=True, verbose_name="Кузов")

    def __str__(self):
        return self.body
    
    class Meta:
        verbose_name = "Кузов"
        verbose_name_plural = "Кузовы"


class Color(models.Model):
    """Цвет."""
    color = models.CharField(max_length=100, blank=True, null=True, verbose_name="Цвет")

    def __str__(self):
        return self.color
    
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Transmission(models.Model):
    """Тип коробки."""
    transmission = models.CharField(max_length=100, blank=True, null=True, verbose_name="Тип коробки")

    def __str__(self):
        return self.transmission


class Availability(models.Model):
    """Доступность."""
    availability = models.CharField(max_length=100, blank=True, null=True, verbose_name="Доступность")

    def __str__(self):
        return self.availability


class Drive(models.Model):
    """Привод."""
    drive = models.CharField(max_length=100, blank=True, null=True, verbose_name="Привод")
    
    def __str__(self):
        return self.drive

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"


class WheelType(models.Model):
    """Руль."""
    wheel_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Рулья")

    def __str__(self):
        return self.wheel_type


class Exchange(models.Model):
    """Вариант обмена."""
    exchange = models.CharField(max_length=100, blank=True, null=True, verbose_name="Обмен")

    def __str__(self):
        return self.exchange


class Registration(models.Model):
    """Учет машины."""
    registration = models.CharField(max_length=100, blank=True, null=True, verbose_name="Учет")

    def __str__(self):
        return self.registration


class CustomClearence(models.Model):
    """Растаможка машины."""
    custom_clearence = models.CharField(max_length=100, blank=True, null=True, verbose_name="Растаможка")

    def __str__(self):
        return self.custom_clearence


class Quickly(models.Model):
    """Срочность."""
    quickly = models.BooleanField(default=False, verbose_name="Срочность")


class Car(models.Model):
    """Машина."""
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория", related_name="cars")
    mark = models.ForeignKey(MarkOfCar, on_delete=models.PROTECT, null=True, verbose_name="Марка", related_name="cars_by_marks")
    model = models.ForeignKey(ModelOfCar, on_delete=models.PROTECT, null=True, verbose_name="Модель", related_name="cars_by_models")
    year = models.ForeignKey(YearOfProduction, on_delete=models.PROTECT, null=True, verbose_name="Год выпуска", related_name="cars_by_years")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    engine = models.ForeignKey(EngineType, on_delete=models.PROTECT, null=True, verbose_name="Двигатель", related_name="cars_by_engines")
    car_condition = models.ForeignKey(CarCondition, on_delete=models.PROTECT, null=True, verbose_name="Состояние", related_query_name="cars_by_conditions", blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, verbose_name="Регион", related_name="cars_by_regions", blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name="Город", related_name="cars_by_cities", blank=True)
    body = models.ForeignKey(BodyType, on_delete=models.PROTECT, null=True, verbose_name="Кузов", related_query_name="cars_by_bodies")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True, verbose_name="Цвет", related_name="colors", blank=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.PROTECT, null=True, verbose_name="Тип коробки", related_query_name="cars_by_transmissions", blank=True)
    drive = models.ForeignKey(Drive, on_delete=models.PROTECT, null=True, verbose_name="Привод", related_name="cars_by_drives", blank=True)
    wheel_type = models.ForeignKey(WheelType, on_delete=models.PROTECT, null=True, verbose_name="Руль", related_name="cars_by_wheel_types", blank=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT, null=True, verbose_name="Обмен", related_name="cars_by_exchanges", blank=True)
    registration = models.ForeignKey(Registration, on_delete=models.PROTECT, null=True, verbose_name="Учет", related_name="cars_by_registrations", blank=True)
    custom_clearence = models.ForeignKey(CustomClearence, on_delete=models.PROTECT, null=True, verbose_name="Растаможка", related_name="cars_by_customs", blank=True)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_available = models.ForeignKey(Availability, on_delete=models.PROTECT, null=True, verbose_name="Доступность", related_name="cars_by_availability")
    is_quickly = models.ForeignKey(Quickly, on_delete=models.PROTECT, null=True, verbose_name="Срочность", related_name="cars_by_quickly")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.mark} {self.model}"


class CarImage(models.Model):
    """Изображение машины."""
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина", related_name='images')
    image = models.ImageField(upload_to='cars_images/', verbose_name="Изображение")
    
    def __str__(self):
        return f"Фото для {self.car}"


class Profile(models.Model):
    """Пользователь."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    number = models.CharField(max_length=20, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to='media/avatar', verbose_name="Аватар")

    def __str__(self):
        return f'Профиль {self.user.username}'
