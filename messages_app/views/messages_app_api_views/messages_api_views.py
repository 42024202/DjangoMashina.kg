from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from messages_app.models import Message, Chat
from messages_app.serializers.message_serializer import MessageSerializer


class MessageListView(generics.ListCreateAPIView):
    "List of messages in chat"
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        user = self.request.user

        if user not in [chat.user1, chat.user2]:
            raise PermissionDenied('You are not in this chat')

        return Message.objects.filter(chat=chat)


class MessageCreateView(generics.CreateAPIView):
    "Create message in chat"
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        sender = self.request.user
        if sender not in [chat.user1, chat.user2]:
            raise PermissionDenied('You are not in this chat')

        recipient = chat.user2 if chat.user1 == sender else chat.user1
        serializer.save(sender=sender, recipient=recipient, chat=chat)

