from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from messages_app.models import Chat


class ChatDetailView(LoginRequiredMixin, TemplateView):
    template_name = "messages_app/chat_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat, pk=chat_id)

        if self.request.user not in [chat.user1, chat.user2]:
            return HttpResponseForbidden("Вы не участник данного чата")

        context['chat'] = chat
        context['other_user'] = chat.get_other_user(self.request.user)
        return context

