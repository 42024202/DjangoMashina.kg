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

