import django_filters
from auto.models import CarAnnouncement, Body, EngineType, EngineCapacity, Transmission, Drive
from common.models import Mark, Model, Generation, Region, City, Condition, Availability
from django.forms import Select
from auto.models.shared.characters import Color, CustomClearence, Exchange, WheelType, Registration


class CarAnnouncementFilter(django_filters.FilterSet):
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

    car_mileage__gte = django_filters.NumberFilter(
        field_name='car_mileage',
        lookup_expr='gte',
        label='Пробег от'
        )

    car_mileage__lte = django_filters.NumberFilter(
        field_name='car_mileage',
        lookup_expr='lte',
        label='Пробег до'
        )

    urgency = django_filters.BooleanFilter(
        field_name='urgency',
        label='Срочно'
        )

    mark = django_filters.ModelChoiceFilter(
        field_name='car_config__mark',
        queryset=Mark.objects.all(),
        label='Марка',
        empty_label='Все марки'
        )

    model = django_filters.ModelChoiceFilter(
        field_name='car_config__model',
        queryset=Model.objects.all(),
        label='Модель',
        empty_label='Все модели'
        )

    generation = django_filters.ModelChoiceFilter(
        field_name='car_config__generation',
        queryset=Generation.objects.all(),
        label='Поколение',
        empty_label='Все поколения'
        )

    body = django_filters.ModelChoiceFilter(
        field_name='car_config__body',
        queryset=Body.objects.all(),
        label='Тип кузова',
        empty_label='Все типы кузова'
        )

    engine_type = django_filters.ModelChoiceFilter(
        field_name='car_config__engine_type',
        queryset=EngineType.objects.all(),
        label='Тип двигателя',
        empty_label='Любой тип'
        )

    engine_capacity = django_filters.ModelChoiceFilter(
        field_name='car_config__engine_capacity',
        queryset=EngineCapacity.objects.all(),
        label='Объем двигателя',
        empty_label='Любой объем'
        )

    engine_power_gte = django_filters.NumberFilter(
        field_name='engine_power',
        lookup_expr='gte',
        label='Мощность двигателя от'
        )

    engine_power_lte = django_filters.NumberFilter(
        field_name='engine_power',
        lookup_expr='lte',
        label='Мощность двигателя до'
        )

    transmission = django_filters.ModelChoiceFilter(
        field_name='car_config__transmission',
        queryset=Transmission.objects.all(),
        label='Коробка передач',
        empty_label='Любая коробка'
        )

    drive = django_filters.ModelChoiceFilter(
        field_name='car_config__drive',
        queryset=Drive.objects.all(),
        label='Тип привода',
        empty_label='Любой привод',
        widget=Select()
        )
    
    color = django_filters.ModelChoiceFilter(
        field_name='color',
        queryset=Color.objects.all(),
        label='Цвет',
        empty_label='Все цвета'
        )

    custom_clearence = django_filters.ModelChoiceFilter(
        field_name='custom_clearence',
        queryset=CustomClearence.objects.all(),
        label='Растаможка',
        empty_label='Растаможка'
        )
    
    exchange = django_filters.ModelChoiceFilter(
        field_name='exchange',
        queryset=Exchange.objects.all(),
        label='Обмен',
        empty_label='Вариант обмена'
        )

    registration = django_filters.ModelChoiceFilter(
        field_name='registration',
        queryset=Registration.objects.all(),
        label='Регистрация',
        empty_label='Регистрация'
        )

    wheel_type = django_filters.ModelChoiceFilter(
        field_name='wheel_type',
        queryset=WheelType.objects.all(),
        label='Тип руля',
        empty_label='Все типы руля'
        )
    
    region = django_filters.ModelChoiceFilter(
        field_name='region',
        queryset=Region.objects.all(),
        label='Регион',
        empty_label='Все регионы'
        )

    city = django_filters.ModelChoiceFilter(
        field_name='city',
        queryset=City.objects.all(),
        label='Город',
        empty_label='Все города'
        )

    car_condition = django_filters.ModelChoiceFilter(
        field_name='car_condition',
        queryset=Condition.objects.all(),
        label='Состояние',
        empty_label='Сосстояние'
        )

    availability = django_filters.ModelChoiceFilter(
        field_name='availability',
        queryset=Availability.objects.all(),
        label='Доступность',
        empty_label='Доступность',
        )

    class Meta:
        model = CarAnnouncement
        fields = [
            'mark', 'model', 'generation',
            'body', 'engine_type', 'engine_capacity',
            'transmission', 'drive', 'color',
            'engine_power_gte', 'engine_power_lte',
            'wheel_type', 'exchange', 'registration', 'urgency',
            'custom_clearence', 'region',
            'city', 'car_condition', 'availability',
        ]

