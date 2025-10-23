from django.db import models


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

