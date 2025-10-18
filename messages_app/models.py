from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from accounts.models import CustomUser 


User = get_user_model()


class Chat(models.Model):
    "Chat between users"
    user1 = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='chat_user1',
            verbose_name='user1'
            )
    user2 = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='chat_user2',
            verbose_name='user2'
            )

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        unique_together = ['user1', 'user2']


    def save(self, *args, **kwargs):
        "user1.id every time will < user2.id"
        if self.user1.id > self.user2.id:
            self.user1, self.user2 = self.user2, self.user1
        super().save(*args, **kwargs)

    def get_other_user(self, current_user):
        """Возвращает собеседника"""
        return self.user2 if self.user1 == current_user else self.user1

    def __str__(self):
        return f"Chat between {self.user1} and {self.user2}"


class Message(models.Model):
    """Message in chat"""
    chat = models.ForeignKey(
            Chat,
            on_delete=models.CASCADE,
            related_name='messages',
            verbose_name='Чат'
            )

    sender = models.ForeignKey(
            User, 
            on_delete=models.CASCADE, 
            related_name='sent_messages'
            )

    recipient = models.ForeignKey(
            User, 
            on_delete=models.CASCADE, 
            related_name='received_messages'
            )

    text = models.TextField(
            verbose_name='Сообщение'
            )

    created_at = models.DateTimeField(
            auto_now_add=True
            )

    is_read = models.BooleanField(
            default=False, 
            verbose_name='Прочитано'
            )

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.text[:20]}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

