from django.db import models


class Category(models.Model):
    """Категория машин."""
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


class CarCondtion(models.Model):
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


class Car(models.Model):
    """Машина."""
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория", related_name="cars")
    mark = models.ForeignKey(MarkOfCar, on_delete=models.PROTECT, null=True, verbose_name="Марка", related_name="cars_by_marks")
    model = models.ForeignKey(ModelOfCar, on_delete=models.PROTECT, null=True, verbose_name="Модель", related_name="cars_by_models")
    year = models.ForeignKey(YearOfProduction, on_delete=models.PROTECT, null=True, verbose_name="Год выпуска", related_name="cars_by_years")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    engine = models.ForeignKey(EngineType, on_delete=models.PROTECT, null=True, verbose_name="Двигатель", related_name="cars_by_engines")
    car_condition = models.ForeignKey(CarCondtion, on_delete=models.PROTECT, null=True, verbose_name="Состояние", related_query_name="cars_by_conditions", blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, verbose_name="Регион", related_name="cars_by_regions", blank=True)
    body = models.ForeignKey(BodyType, on_delete=models.PROTECT, null=True, verbose_name="Кузов", related_query_name="cars_by_bodies")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True, verbose_name="Цвет", related_name="colors", blank=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.PROTECT, null=True, verbose_name="Тип коробки", related_query_name="cars_by_transmissions", blank=True)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    images = models.ImageField(upload_to='media/cars_image', verbose_name="Фотография")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.mark} {self.model}"
