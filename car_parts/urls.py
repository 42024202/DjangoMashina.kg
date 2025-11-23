from django.urls import path
from .views.delete_views import PartsDeleteView
from .views.detail_views import PartsAndConsumbleDetailView

app_name = 'car_parts'

urlpatterns = [
    path("detail/<int:pk>/",PartsAndConsumbleDetailView.as_view(),name="consumble_detail"),
    path("delete/<str:model_name>/<int:pk>/",PartsDeleteView.as_view(),name="delete_announcement")
    ]

