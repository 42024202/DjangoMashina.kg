from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("car_detail/<int:car_id>/<slug:car_slug>", views.CarDetailView.as_view(), name="car_detail"),
    path("category/<str:category_name>", views.CategoryView.as_view(), name="category"),
    path("delete_announcement/<int:car_id>", views.IndexView.as_view(), name="delete_announcement"),
    path('get_my_announcements/', views.MyAnnouncementsView.as_view(), name='get_my_announcements'),
    path('create_announcement/', views.CreateAnnouncementView.as_view(), name='create_announcement'),
    ]

