from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    number = models.CharField(max_length=20, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to='avatar/', verbose_name="Аватар")

    def __str__(self):
        return f'Профиль {self.user.username}'
