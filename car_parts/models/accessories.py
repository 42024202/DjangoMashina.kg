from django.db import models 
from accounts.models import CustomUser
from common.models import ( 
        Mark, Model, Generation,
        Region, City, Condition, Availability
            )


class CarAccessorie(models.Model):
    name = models.CharField(
            max_length=30,
            verbose_name='Название'
            )
    profile = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name='Профиль'
            )

    mark = models.ForeignKey(
            Mark, 
            on_delete=models.PROTECT, 
            verbose_name='Марка'
            )
    model = models.ForeignKey(
            Model, 
            on_delete=models.PROTECT, 
            verbose_name='Модель'
            )
    generation = models.ForeignKey(
            Generation, 
            on_delete=models.PROTECT, 
            verbose_name='Поколение'
            )
    price = models.DecimalField(
            max_digits=9,
            decimal_places=1,
            verbose_name='Цена'
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
    condition = models.ForeignKey(
            Condition, 
            on_delete=models.PROTECT, 
            verbose_name='Состояние'
            )
    availability = models.ForeignKey(
            Availability, 
            on_delete=models.PROTECT, 
            verbose_name='Доступность'
            )
    description = models.TextField(
            verbose_name='Описание'
            )

    def __str__(self):
        return f"{self.name} {self.mark} {self.model} {self.generation}"

    class Meta:
        verbose_name = 'Аксессуар и мультимедиа'
        verbose_name_plural = 'Аксессуары и мультимедиа'
        ordering = ['-id']
        

class CarAccessoriesImage(models.Model):
    image = models.ImageField(
            upload_to='accessories_images/',
            verbose_name='Фото'
            )

    accessories = models.ForeignKey(
            CarAccessorie, 
            on_delete=models.CASCADE, 
            related_name='images',
            )

