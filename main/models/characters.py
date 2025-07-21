from django.db import models


class EngineType(models.Model):
    """Engine type of car."""
    engine_name = models.CharField(max_length=40, verbose_name="Тип двигателя")
    

    class Meta:
        verbose_name = "Тип двигателя"
        verbose_name_plural = "Тип двигателей"

    def __str__(self):
        return self.engine_name


class EngineCapacity(models.Model):
    """Engine capacity of car."""
    engine_capacity = models.DecimalField(decimal_places=1, max_digits=2,verbose_name="Объем двигателя")
    

    class Meta:
        verbose_name = "Объем двигателя"
        verbose_name_plural = "Объем двигателя"

    def __str__(self):
        return str(self.engine_capacity)


class EnginePower(models.Model):
    engine_power = models.DecimalField(max_digits=4, decimal_places=1,verbose_name="Мощность двигателя")
    

    class Meta:
        verbose_name = "Мощность двигателя"
        verbose_name_plural = "Мощность двигателя"

    def __str__(self):
        return str(self.engine_power)


class BodyType(models.Model):
    """Body type of car."""
    body_type_name = models.CharField(max_length=40, verbose_name="Тип кузова")
    
    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Тип кузовов"

    def __str__(self):
        return self.body_type_name


class Drive(models.Model):
    """Drive type of car."""
    drive_name = models.CharField(max_length=40, verbose_name="Тип привода")
    

    class Meta:
        verbose_name = "Тип привода"
        verbose_name_plural = "Тип приводов"

    def __str__(self):
        return self.drive_name


class WheelType(models.Model):
    """Wheel type of car."""
    wheel_type_name = models.CharField(max_length=40, verbose_name="Руль")
    

    class Meta:
        verbose_name = "Тип руля"
        verbose_name_plural = "Тип руля"

    def __str__(self):
        return self.wheel_type_name


class Transmission(models.Model):
    """Transmission type of car."""
    transmission_name = models.CharField(max_length=40, verbose_name="Коробка передач")
    
    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробка передач"

    def __str__(self):
        return self.transmission_name

