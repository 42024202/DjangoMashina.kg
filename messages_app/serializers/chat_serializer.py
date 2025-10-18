from rest_framework import serializers
from ..models import Chat
from .user_serializer import UserSerializer
from .message_serializer import MessageSerializer

class ChatSerializer(serializers.ModelSerializer):
    user1 = UserSerializer(read_only=True)
    user2 = UserSerializer(read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ['user1', 'user2', 'last_message']

    def get_last_message(self, obj):
        last_message = obj.messages.last()
        return MessageSerializer(last_message).data if last_message else None

