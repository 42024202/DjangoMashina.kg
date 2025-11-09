from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.FavoriteListView.as_view(), name='favorites'),
    path('toggle/<str:app_label>/<str:model_name>/<int:object_id>/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    ]

