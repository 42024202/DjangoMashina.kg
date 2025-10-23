from django.urls import path

#APIES
from .views.messages_app_api_views.chat_api_views import ChatApiCreateView, ChatApiListView
from .views.messages_app_api_views.messages_api_views import MessageApiListView, MessageApiCreateView
from .views.messages_app_api_views.user_api_views import UserApiListView

#TEMPLATES
from .views.messages_app_views.chat_detail_views import ChatDetailView
from .views.messages_app_views.chat_list_views import ChatListView

urlpatterns = [
    #APIES
    path('usrers/', UserApiListView.as_view(), name='user-list'),

    path('chats-api/', ChatApiListView.as_view(), name='chat-list-api'),
    path('chats-api/create/', ChatApiCreateView.as_view(), name='chat-create'),

    path('chats-api/<int:chat_id>/messages/', MessageApiListView.as_view(), name='message-list'),
    path('chats-api/<int:chat_id>/messages/send/', MessageApiCreateView.as_view(), name='message-send'),


    #TEMPLATES
    path('chats/', ChatListView.as_view(), name='chat-list'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat-detail'),

    ]

