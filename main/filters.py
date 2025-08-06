import django_filters
from main.models import CarAnnouncement
from common.models import Mark, Model, Generation
from main.models.car_config import Body, EngineType, EngineCapacity, Transmission, Drive


class CarAnnouncenmentFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(
            field_name='price', 
            lookup_expr='gte'
            )

    price__lte = django_filters.NumberFilter(
            field_name='price', 
            lookup_expr='lte'
            )

    year__gte = django_filters.NumberFilter(
            field_name='year', 
            lookup_expr='gte'
            )

    year__lte = django_filters.NumberFilter(
            field_name='year', 
            lookup_expr='lte'
            )

    mark = django_filters.ModelChoiceFilter(
            field_name='car_config__mark', 
            queryset=Mark.objects.all()
            )

    model = django_filters.ModelChoiceFilter(
            field_name='car_config__model', 
            queryset=Model.objects.all()
            )

    generation = django_filters.ModelChoiceFilter(
            field_name='car_config__generation', 
            queryset=Generation.objects.all()
            )

    body = django_filters.ModelChoiceFilter(
            field_name='car_config__body', 
            queryset=Body.objects.all()
            )

    engine_type = django_filters.ModelChoiceFilter(
            field_name='car_config__engine_type', 
            queryset=EngineType.objects.all()
            )

    engine_capacity = django_filters.ModelChoiceFilter(
            field_name='car_config__engine_capacity', 
            queryset=EngineCapacity.objects.all()
            )

    transmission = django_filters.ModelChoiceFilter(
            field_name='car_config__transmission', 
            queryset=Transmission.objects.all()
            )

    drive = django_filters.ModelChoiceFilter(
            field_name='car_config__drive', 
            queryset=Drive.objects.all()
            )

    class Meta:
        model = CarAnnouncement
        fields = ['mark', 'model', 'generation',
                  'body', 'engine_type', 'engine_capacity',
                  'transmission', 'drive',
                  'color', 'engine_power', 'car_mileage', 
                  'wheel_type', 'exchange', 'registration', 
                  'custom_clearence', 'urgency', 'region', 
                  'city', 'car_condition', 'availability',
                ]

