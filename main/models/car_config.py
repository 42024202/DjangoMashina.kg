from django.db import models


class Body(models.Model):
    """Type of body of car"""
    name = models.CharField(
            max_length=40, 
            verbose_name="Тип кузова"
            )

    verbose_name = "Тип кузова"
    verbose_name_plural = "Тип кузовов"
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Тип кузовов"


class EngineType(models.Model):
    """Type of engine of car"""
    name = models.CharField(
            max_length=40, 
            verbose_name="Тип двигателя"
            )

    class Meta:
        verbose_name = "Тип двигателя"
        verbose_name_plural = "Тип двигателей"
    
    def __str__(self):
        return self.name


class EngineCapacity(models.Model):
    """Capacity of engine of car"""
    capacity = models.DecimalField(
            max_digits=2, 
            decimal_places=1, 
            verbose_name="Объем двигателя"
            )

    class Meta:
        verbose_name = "Объем двигателя"
        verbose_name_plural = "Объем двигателей"

    def __str__(self):
        return str(self.capacity)


class Transmission(models.Model):
    """Type of transmission of car"""
    name = models.CharField(
            max_length=40, 
            verbose_name="Коробка передач"
            )

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробки передач"

    def __str__(self):
        return self.name


class Drive(models.Model):
    """Type of drive"""
    name = models.CharField(
            max_length=40, 
            verbose_name="Тип привода"
            )

    class Meta:
        verbose_name = "Тип привода"
        verbose_name_plural = "Типы привода"

    def __str__(self):
        return self.name


class CarConfig(models.Model):
    """Configuration of car"""
    mark = models.ForeignKey(
            'common.Mark', 
            on_delete=models.PROTECT, 
            verbose_name="Марка"
            )

    model = models.ForeignKey(
            'common.Model', 
            on_delete=models.PROTECT, 
            verbose_name="Модель"
            )

    generation = models.ForeignKey(
            'common.Generation', 
            on_delete=models.PROTECT, 
            verbose_name="Поколение"
            )

    body = models.ForeignKey(
            Body, 
            on_delete=models.PROTECT, 
            verbose_name="Тип кузова"
            )

    engine_type = models.ForeignKey(
            EngineType, 
            on_delete=models.PROTECT, 
            verbose_name="Тип двигателя"
            )

    engine_capacity = models.ForeignKey(
            EngineCapacity, 
            on_delete=models.PROTECT, 
            verbose_name="Объем двигателя"
            )
    transmission = models.ForeignKey(
            Transmission, 
            on_delete=models.PROTECT, 
            verbose_name="Коробка передач"
            )

    drive = models.ForeignKey(
            Drive, 
            on_delete=models.PROTECT, 
            verbose_name="Тип привода"
            )
    
    def __str__(self):
        return f"{self.mark} {self.model} {self.generation} {self.body} {self.engine_type} {self.engine_capacity}"

    class Meta:
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурации"

