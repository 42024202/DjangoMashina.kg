from django.urls import path
from .views.chat_views import ChatListView, ChatCreateView
from .views.messages_views import MessageListView, MessageCreateView
from .views.user_views import UserListView

urlpatterns = [
    path('usrers/', UserListView.as_view(), name='user-list'),

    path('chats/', ChatListView.as_view(), name='chat-list'),
    path('chats/create/', ChatCreateView.as_view(), name='chat-create'),

    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('chats/<int:chat_id>/messages/send/', MessageCreateView.as_view(), name='message-send'),
    
    ]

