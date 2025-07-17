from django.db import models


class Category(models.Model):
    """Категория машин."""
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название")
    
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Car(models.Model):
    """Машины."""
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Категория")
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name="Модель")
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True, blank=True, verbose_name="Цена")
    image = models.ImageField(upload_to='media/cars', null=True, blank=True, verbose_name="Фотография")
    year = models.DateField(verbose_name="Год выпуска")
    

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return self.title

