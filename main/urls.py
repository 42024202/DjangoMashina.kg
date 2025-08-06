from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("car_detail/<int:car_id>", views.car_detail, name="car_detail"),
    path("category/<str:category_name>", views.category_view, name="category"),
    path("add_announcement", views.index, name="add_announcement"),
    path("delete_announcement/<int:car_id>", views.index, name="delete_announcement"),
    path('get-models/', views.index, name='get_models'),
    ]

