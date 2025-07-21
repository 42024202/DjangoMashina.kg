from django.db import models


class Category(models.Model):
    """Category of car with hierarchy"""
    cateory_name = models.CharField(max_length=50, verbose_name="Категория")
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
        return self.cateory_name


class MarkOfCar(models.Model):
    """Mark of car."""
    mark_name = models.CharField(max_length=50, verbose_name="Марка")

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return self.mark_name


class ModelOfCar(models.Model):
    """Model of car."""
    model_name = models.CharField(max_length=50, verbose_name="Модель")
    mark = models.ForeignKey(MarkOfCar, on_delete=models.PROTECT, verbose_name="Марка")

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return self.model_name
