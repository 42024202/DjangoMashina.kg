from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model
from ..models import Chat
from ..serializers.chat_serializer import ChatSerializer


User = get_user_model()

class ChatListView(generics.ListAPIView):
    "List of all chats for current user"
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(user1=user) | Q(user2=user))


class ChatCreateView(generics.CreateAPIView):
    "Create new chat with current user and another user"
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        other_user_id = request.data.get('user2_id')
        if not other_user_id:
            return Response(
                {'error': 'User2 id is required'},
                status=status.HTTP_400_BAD_REQUEST
                )
        user = request.user

        try:
            other_user = User.objects.get(id=other_user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user1, user2 = sorted([user, other_user], key=lambda u: u.id)
        chat, created = Chat.objects.get_or_create(user1=user1, user2=user2)
        
        return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)

