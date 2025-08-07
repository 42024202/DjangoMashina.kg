import django_filters
from auto.models import CarAnnouncement
from common.models import Mark, Model, Generation
from auto.models import Body, EngineType, EngineCapacity, Transmission, Drive


class CarAnnouncenmentFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(
            field_name='price', 
            lookup_expr='gte',
            label='Цена от'
            )

    price__lte = django_filters.NumberFilter(
            field_name='price', 
            lookup_expr='lte',
            label='Цена до' 
            )

    year__gte = django_filters.NumberFilter(
            field_name='year', 
            lookup_expr='gte',
            label='Год выпуска от'
            )

    year__lte = django_filters.NumberFilter(
            field_name='year', 
            lookup_expr='lte',
            label='Год выпуска до'
            )

    mark = django_filters.ModelChoiceFilter(
            field_name='car_config__mark', 
            queryset=Mark.objects.all(),
            label='Марка'
            )

    model = django_filters.ModelChoiceFilter(
            field_name='car_config__model', 
            queryset=Model.objects.all(),
            label='Модель'
            )

    generation = django_filters.ModelChoiceFilter(
            field_name='car_config__generation', 
            queryset=Generation.objects.all(),
            label='Поколение'
            )

    body = django_filters.ModelChoiceFilter(
            field_name='car_config__body', 
            queryset=Body.objects.all(),
            label='Тип кузова'
            )

    car_mileage__lte = django_filters.NumberFilter(
            field_name='car_mileage',
            lookup_expr='lte',
            label='Пробег до'
            )
    car_mileage__gte = django_filters.NumberFilter(
            field_name='car_mileage',
            lookup_expr='gte',
            label='Пробег от'
            )

    engine_type = django_filters.ModelChoiceFilter(
            field_name='car_config__engine_type', 
            queryset=EngineType.objects.all(),
            label='Тип двигателя'
            )

    engine_power_lte = django_filters.NumberFilter(
            field_name='engine_power',
            lookup_expr='lte',
            label='Мощность двигателя до'
            )
    engine_power_gte = django_filters.NumberFilter(
            field_name='engine_power',
            lookup_expr='gte',
            label='Мощность двигателя от'
            )

    engine_capacity = django_filters.ModelChoiceFilter(
            field_name='car_config__engine_capacity', 
            queryset=EngineCapacity.objects.all(),
            label='Объем двигателя'
            )

    transmission = django_filters.ModelChoiceFilter(
            field_name='car_config__transmission', 
            queryset=Transmission.objects.all(),
            label='Коробка передач'
            )

    drive = django_filters.ModelChoiceFilter(
            field_name='car_config__drive', 
            queryset=Drive.objects.all(),
            label='Тип привода'
            )

    class Meta:
        model = CarAnnouncement
        fields = ['mark', 'model', 'generation',
                  'body', 'engine_type', 'engine_capacity',
                  'transmission', 'drive','color',
                  'engine_power_gte','engine_power_lte',
                  'wheel_type',
                  'exchange', 'registration', 
                  'custom_clearence', 'urgency', 'region', 
                  'city', 'car_condition', 'availability',
                ]

