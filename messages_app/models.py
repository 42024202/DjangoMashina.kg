from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from accounts.models import CustomUser 


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

