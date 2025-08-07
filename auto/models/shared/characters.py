from django.db import models


class Category(models.Model):
    """Category of car with hierarchy"""
    name = models.CharField(
            max_length=50,
            verbose_name="Категория"
            )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT, 
        null=True, blank=True,
        related_name= 'subcategory',
        verbose_name="Родительская категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name


class WheelType(models.Model):
    """Wheel type of car."""
    wheel_type_name = models.CharField(
            max_length=40, 
            verbose_name="Руль"
            )

    class Meta:
        verbose_name = "Тип руля"
        verbose_name_plural = "Тип руля"

    def __str__(self):
        return self.wheel_type_name


class Exchange(models.Model):
    """Exchange option"""
    name = models.CharField(
            max_length=40, 
            verbose_name="Вариант обмена"
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вариант обмена"
        verbose_name_plural = "Вариант обмена"


class YearOfProduction(models.Model):
        year = models.PositiveBigIntegerField(
                verbose_name="Год выпуска"
                )

        def __str__(self):
            return str(self.year)

        class Meta:
            verbose_name = "Год выпуска"
            verbose_name_plural = "Год выпуска"


class Color(models.Model):
    name = models.CharField(
            max_length=40, 
            verbose_name="Цвет"
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвет"


class Registration(models.Model):
    registration = models.CharField(
            max_length=50, 
            verbose_name="Учет"
            )

    def __str__(self):
        return self.registration

    class Meta:
        verbose_name = "Учет"
        verbose_name_plural = "Учет"


class CustomClearence(models.Model):
    custom_clearence = models.BooleanField(
            default=True, 
            verbose_name="Растаможка"
            )

    def __str__(self):
        if self.custom_clearence:
            return "Растаможен"
        else:
            return "Нерастаможен"

    class Meta:
        verbose_name = "Растаможка"
        verbose_name_plural = "Растаможка"

