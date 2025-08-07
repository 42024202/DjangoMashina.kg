from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import CustomUser


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


