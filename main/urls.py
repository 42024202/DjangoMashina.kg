from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("car_detail/<int:car_id>", views.car_detail, name="car_detail"),
    path("category/<str:category_name>", views.category, name="category"),
    path("add_announcement", views.add_announcement, name="add_announcement"),
    path("delete_announcement/<int:car_id>", views.delete_announcement, name="delete_announcement"),
    path('get-models/', views.get_models, name='get_models'),
    ]
