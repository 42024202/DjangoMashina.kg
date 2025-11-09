from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import CustomUser
from django.contrib.auth import get_user_model


user = get_user_model()

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
    
    def __str__(self):
        return f"{self.user} → {self.content_object}"


    class Meta:
        unique_together = ('user', 
                           'content_type', 
                           'object_id'
                           )

        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

