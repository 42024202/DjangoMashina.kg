from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("car_detail/<int:car_id>", views.car_detail, name="car_detail"),
    path("passenger_cars", views.passenger_cars, name="passenger_cars"),
    path("moto_cars", views.moto_cars, name="moto_cars"),
    path("commercial_cars", views.commercial_cars, name="commercial_cars"),
    ] 
