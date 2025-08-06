from django.db import models
import random, uuid
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
            self, 
            email, 
            password=None, 
            **extra_fields
            ):
        if not email:
            raise ValueError('Email обязателен для регистрации')
        email = self.normalize_email(email)
        user = self.model(
                email=email, 
                **extra_fields
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, 
            email, 
            password=None, 
            **extra_fields
            ):

        extra_fields.setdefault(
                'is_staff', 
                True
                )

        extra_fields.setdefault(
                'is_superuser', 
                True
                )

        extra_fields.setdefault(
                'is_active',
                True
                )

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                    'Superuser должен иметь is_staff=True.'
                )

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                    'Superuser должен иметь is_superuser=True.'
                )

        return self.create_user(
                email, 
                password, 
                **extra_fields
                )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
            max_length=30,
            verbose_name='Имя пользователя'
            )

    email = models.EmailField(
            unique=True, 
            verbose_name='Электронная почта'
            )

    phone = models.CharField(
            max_length=30,
            blank=True, 
            null=True, 
            verbose_name='Телефон'
            )
    avatar = models.ImageField(
            upload_to='avatars/', 
            blank=True, 
            null=True, 
            verbose_name='Аватар'
            )

    is_verified = models.BooleanField(
            default=False, 
            verbose_name='Подтвержден'
            )

    is_staff = models.BooleanField(
            default=False, 
            verbose_name='Сотрудник'
            )

    is_active = models.BooleanField(
            default=True, 
            verbose_name='Активен'
            )

    date_joined = models.DateTimeField(
            default=timezone.now, 
            verbose_name='Дата регистрации'
            )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


def generate_unique_account_number():
    """Generate unique 6-digit account number"""
    while True:
        number = f"{random.randint(100000, 999999)}"
        if not Balance.objects.filter(account_number=number).exists():
            return number


class EmailOTP(models.Model):
    user = models.CharField(
            max_length=255,
            verbose_name='Пользователь'
            )

    code = models.CharField(
            max_length=6
            )

    created_at = models.DateTimeField(
            auto_now_add=True
            )

    is_used = models.BooleanField(
            default=False
            )

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=3)

    class Meta:
        verbose_name = 'Одноразовый код'
        verbose_name_plural = 'Одноразовый код'


class Balance(models.Model):
    """Users balance"""
    user = models.OneToOneField(
            'CustomUser', 
            on_delete=models.CASCADE, 
            related_name='balance'
            )
    
    amount = models.DecimalField(
            max_digits=12, 
            decimal_places=2, 
            default=0
            )

    account_number = models.CharField(
            max_length=6, 
            unique=True, 
            blank=True
            )


    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = generate_unique_account_number()
        super().save(*args, **kwargs)

    def has_enough(self, value):
        """Check amount of balance"""
        return self.amount >= value

    def deposit(self, value):
        """Change amount of balance"""
        if value <= 0:
            raise ValueError(
                    "Сумма пополнения должна быть положительной"
                    )

        self.amount += value
        self.save()

    def withdraw(self, value):
        """Make withdraw from balance"""
        if value <= 0:
            raise ValueError(
                    "Сумма списания должна быть положительной"
                    )

        if self.amount < value:
            raise ValueError(
                    "Недостаточно средств"
                    )

        self.amount -= value
        self.save()

    def __str__(self):
        return f"{self.user.username} — {self.account_number}: {self.amount} сом"
    
    class Meta:
        verbose_name = "Баланс"
        verbose_name_plural = "Баланс"


User = get_user_model()

class Message(models.Model):
    """For message between users"""
    sender = models.ForeignKey(
            CustomUser, 
            on_delete=models.CASCADE, 
            related_name='sent_messages'
            )

    recipient = models.ForeignKey(
            User, 
            on_delete=models.CASCADE, 
            related_name='received_messages'
            )

    content = models.TextField(
            verbose_name='Сообщение'
            )

    timestamp = models.DateTimeField(
            auto_now_add=True
            )

    is_read = models.BooleanField(
            default=False, 
            verbose_name='Прочитано'
            )

    def __str__(self):
        return f"От {self.sender} к {self.recipient} — {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Favorite(models.Model):
    """Users favorites announcements"""
    user = models.ForeignKey(
            CustomUser, 
            on_delete=models.CASCADE, 
            related_name='favorites'
            )

    content_type = models.ForeignKey(
            ContentType, 
            on_delete=models.CASCADE
            )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
            'content_type', 
            'object_id')

    added_at = models.DateTimeField(
            auto_now_add=True
            )
    
    def is_favorite(user, obj):
        """Check is favorite or not"""
        ct = ContentType.objects.get_for_model(obj)
        return Favorite.objects.filter(
            user=user, 
            content_type=ct, 
            object_id=obj.pk).exists()
        
    def __str__(self):
        return f"{self.user} → {self.content_object}"


    class Meta:
        unique_together = ('user', 
                           'content_type', 
                           'object_id'
                           )

        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"


class Transaction(models.Model):
    """Transactions"""
    name = models.CharField(
            max_length=255, 
            verbose_name='Название транзакции'
            )

    user = models.ForeignKey(
            CustomUser, 
            on_delete=models.CASCADE, 
            related_name='transactions', 
            verbose_name='Профиль'
            )

    balance = models.ForeignKey(
            Balance, 
            on_delete=models.CASCADE, 
            related_name='transactions', 
            verbose_name='Баланс'
            )

    amount = models.DecimalField(
            max_digits=10, 
            decimal_places=2, 
            verbose_name='Сумма'
            )

    description = models.TextField(
            blank=True, 
            verbose_name='Описание тарифа'
            )

    created_at = models.DateTimeField(
            auto_now_add=True, 
            verbose_name='Дата создания'
            )

    def __str__(self):
        return f"{self.name} — {self.amount}"

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

