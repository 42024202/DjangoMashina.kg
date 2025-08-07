from django.db import models 


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

