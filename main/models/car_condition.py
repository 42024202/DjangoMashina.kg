from django.db import models


class YearOfProduction(models.Model):
    """year of production of car."""
    year_of_production = models.CharField(max_length=100, verbose_name="Год выпуска")

    def __str__(self):
        return self.year_of_production

    class Meta:
        verbose_name = "Год выпуска"
        verbose_name_plural = "Год выпуска"


class ColorOfCar(models.Model):
    color_of_car = models.CharField(max_length=100, verbose_name="Цвет машины")

    def __str__(self):
        return self.color_of_car

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвет"
 

class CarMeleage(models.Model):
    car_meleage = models.PositiveIntegerField(verbose_name="Пробег машины")
    
    def __str__(self):
        return str(self.car_meleage)

    class Meta:
        verbose_name = "Пробег"
        verbose_name_plural = "Пробег"


class CarCondition(models.Model):
    """Condition of car."""
    condition = models.CharField(max_length=100, verbose_name="Состояние")

    def __str__(self):
        return self.condition

    class Meta:
        verbose_name = "Состояние"
        verbose_name_plural = "Состояния"
