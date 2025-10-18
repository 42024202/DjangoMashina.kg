from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from messages_app.models import Chat


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'messages_app/chat_list.html'

    def get_queryset(self):
        return Chat.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
