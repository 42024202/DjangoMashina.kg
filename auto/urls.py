from django.urls import path
from .views.index_category.auto_index import IndexView
from .views.index_category.auto_category_view import CategoryView

from .views.crud_views.choise_creating_view import get_announcement_create
from .views.crud_views.create_car_view import CreateCarAnnouncementView
from .views.crud_views.create_moto_view import CreateMotoAnnouncementView

from .views.crud_views.car_detail_view import CarDetailView
from .views.crud_views.moto_detail_view import MotoDetailView

from .views.crud_views.update_car_view import UpdateCarAnnouncementView
from .views.crud_views.update_moto_view import UpdateMotoAnnouncementView

from .views.crud_views.delete_announcements_view import DeleteAnnouncementView


app_name = 'auto'
urlpatterns = [
    #Index and Category urls
    path("", IndexView.as_view(), name="index"),
    path("category/<str:category_name>", CategoryView.as_view(), name="category"),

    #CRUD urls:
    #creating urls
    path('choise_creating_announcement/', get_announcement_create, name='get_creating_announcement'),
    path('create_car_announcement/', CreateCarAnnouncementView.as_view(), name='create_car_announcement'),
    path('create_moto_announcement/', CreateMotoAnnouncementView.as_view(), name='create_moto_announcement'),

    #detail urls
    path("car_detail/<int:car_id>/<slug:car_slug>", CarDetailView.as_view(), name="car_detail"),
    path("moto_detail/<int:moto_id>/<slug:moto_slug>", MotoDetailView.as_view(), name="moto_detail"),

    #update urls
    path('update_car_announcement/<int:car_id>/', UpdateCarAnnouncementView.as_view(), name='update_car_announcement'),
    path('update_moto_announcement/<int:moto_id>/', UpdateMotoAnnouncementView.as_view(), name='update_moto_announcement'),

    #delete ursl
    path('delete_announcement/<str:model_name>/<int:pk>/', DeleteAnnouncementView.as_view(), name='delete_announcement'),
       ]

