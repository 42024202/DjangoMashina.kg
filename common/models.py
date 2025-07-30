from django.db import models


class Region(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Название региона'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регион'


class City(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Название города'
            )

    region = models.ForeignKey(
            Region, 
            on_delete=models.PROTECT, 
            verbose_name='Регион'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'


class Condition(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Состояние'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'


class Avalability(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Доступность'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доступность'
        verbose_name_plural = 'Доступность'


class Mark(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Марка'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марка'


class Model(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Модель'
            )

    mark = models.ForeignKey(
            Mark, 
            on_delete=models.PROTECT, 
            verbose_name='Марка', 
            related_name='models_by_mark'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Generation(models.Model):
    name = models.CharField(
            max_length=30, 
            verbose_name='Поколение'
            )

    model = models.ForeignKey(
            Model, 
            on_delete=models.PROTECT, 
            verbose_name='Модель'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколение'

