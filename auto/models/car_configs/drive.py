from django.db import models


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

