from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("car_detail/<int:car_id>/<slug:car_slug>", views.CarDetailView.as_view(), name="car_detail"),
    path("category/<str:category_name>", views.CategoryView.as_view(), name="category"),
    path('get_my_announcements/', views.MyAnnouncementsView.as_view(), name='get_my_announcements'),

    path('choise_creating_announcement/', views.get_announcement_create, name='get_creating_announcement'),
    path('create_announcement/', views.CreateAnnouncementView.as_view(), name='create_announcement'),
    path('update_announcement/<int:car_id>/', views.UpdateAnnouncementView.as_view(), name='update_announcement'),
    path('delete_announcement/<int:car_id>/', views.DeleteAnnouncementView.as_view(), name='delete_announcement'),
    ]

