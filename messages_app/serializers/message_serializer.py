from rest_framework import serializers
from ..models import Message
from .user_serializer import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['chat', 'sender', 'recipient', 'text', 'created_at', 'is_read']
        read_only_fields = ['chat', 'sender', 'recipient', 'created_at', 'is_read']

