from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorites_announcenments_view, name='favorites'),
    path('toggle/<int:car_id>/', views.toggle_favorite, name='toggle'),
    ]

