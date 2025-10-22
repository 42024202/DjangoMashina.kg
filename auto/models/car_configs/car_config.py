from django.db import models
from ..car_configs.body import Body
from ..car_configs.drive import Drive
from ..car_configs.engine import EngineType, EngineCapacity
from ..car_configs.transmission import Transmission


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

        unique_together = (
                'mark', 'model', 'generation',
                'body', 'engine_type', 'engine_capacity',
                'transmission', 'drive'
                )

