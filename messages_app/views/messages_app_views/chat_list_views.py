from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model


User = get_user_model()

class ChatListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'messages_app/chat_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

