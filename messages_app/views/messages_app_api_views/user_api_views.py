from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from messages_app.serializers.user_serializer import UserSerializer


User = get_user_model()


class UserApiListView(generics.ListAPIView):
    "List of all users except current user"
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

