from django.db import models 
from accounts.models import CustomUser
from common.models import (
        Region, City
        )


class StateNumber(models.Model):
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name='Профиль'
            )

    price = models.DecimalField(
            max_digits=9,
            decimal_places=1,
            verbose_name='Цена'
            )

    number = models.CharField(
            max_length=10,
            verbose_name='Номер'
            )

    region = models.ForeignKey(
            Region,
            on_delete=models.PROTECT,
            verbose_name='Регион'
            )

    city = models.ForeignKey(
            City,
            on_delete=models.PROTECT,
            verbose_name='Город'
            )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Госномер'
        verbose_name_plural = 'Госномера'
        ordering = ['-id']


class StateNumberImage(models.Model):
    state_number = models.ForeignKey(
            StateNumber,
            on_delete=models.CASCADE,
            verbose_name='Госномер'
            )

    image = models.ImageField(
            upload_to='state_numbers',
            verbose_name='Фото'
            )

    def __str__(self):
        return self.state_number

    class Meta:
        verbose_name = 'Фото госномер'
        verbose_name_plural = 'Фото госномеров'

