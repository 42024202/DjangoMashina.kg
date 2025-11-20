from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("car_detail/<int:car_id>/<slug:car_slug>", views.CarDetailView.as_view(), name="car_detail"),
    path("moto_detail/<int:moto_id>/<slug:moto_slug>", views.MotoDetailView.as_view(), name="moto_detail"),

    path("category/<str:category_name>", views.CategoryView.as_view(), name="category"),
    path('get_my_announcements/', views.MyAnnouncementsView.as_view(), name='get_my_announcements'),

    path('choise_creating_announcement/', views.get_announcement_create, name='get_creating_announcement'),
    path('create_car_announcement/', views.CreateAnnouncementView.as_view(), name='create_car_announcement'),
    path('update_car_announcement/<int:car_id>/', views.UpdateAnnouncementView.as_view(), name='update_car_announcement'),
    path('delete_announcement/<str:model_name>/<int:pk>/', views.DeleteAnnouncementView.as_view(), name='delete_announcement'),
    path('create_moto_announcement/', views.CreateMotoAnnouncementView.as_view(), name='create_moto_announcement'),
    ]

