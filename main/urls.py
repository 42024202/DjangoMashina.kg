from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("car_detail/<int:car_id>", views.car_detail, name="car_detail"),
    path("category/<str:category_name>", views.category, name="category"),
    ]
