from django.contrib import admin
from .models import Message, Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2')
    search_fields = ('user1__email', 'user2__email')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'is_read')
    search_fields = ('sender__email', 'recipient__email')
    list_filter = ('is_read',)

