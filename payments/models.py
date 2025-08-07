from django.db import models
from accounts.models import CustomUser
from accounts.models import generate_unique_account_number

class Balance(models.Model):
    """Users balance"""
    user = models.OneToOneField(
            CustomUser, 
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

