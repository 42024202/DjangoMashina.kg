from django.urls import path

#APIES
from .views.messages_app_api_views.chat_api_views import ChatListView, ChatCreateView
from .views.messages_app_api_views.messages_api_views import MessageListView, MessageCreateView
from .views.messages_app_api_views.user_api_views import UserListView

#TEMPLATES
from .views.messages_app_views.chat_detail_views import ChatDetailView
from .views.messages_app_views.chat_list_views import ChatListView

urlpatterns = [
    #APIES
    path('usrers/', UserListView.as_view(), name='user-list'),

    path('chats/', ChatListView.as_view(), name='chat-list'),
    path('chats/create/', ChatCreateView.as_view(), name='chat-create'),

    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('chats/<int:chat_id>/messages/send/', MessageCreateView.as_view(), name='message-send'),

    #TEMPLATES
    path('chats/', ChatListView.as_view(), name='chat-list'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat-detail'),

    ]

