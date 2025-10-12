import django_filters
from auto.models import CarAnnouncement, Body, EngineType, EngineCapacity, Transmission, Drive
from common.models import Mark, Model, Generation


class CarAnnouncementFilter(django_filters.FilterSet):
    # --- Цена ---
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

    # --- Год выпуска ---
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

    # --- Пробег ---
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

    # --- Марка / Модель / Поколение ---
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

    # --- Кузов ---
    body = django_filters.ModelChoiceFilter(
        field_name='car_config__body',
        queryset=Body.objects.all(),
        label='Тип кузова',
        empty_label='Все типы кузова'
        )

    # --- Двигатель ---
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

    # --- Трансмиссия и привод ---
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
        empty_label='Любой привод'
        )

    color = django_filters.CharFilter(
        field_name='color',
        lookup_expr='icontains',
        label='Цвет'
        )

    color = django_filters.ChoiceFilter(
        field_name='color',
        choices=lambda: CarAnnouncement.objects
            .values_list('color', 'color')
            .distinct(),
        label='Цвет',
        empty_label='Все цвета'
        )

    wheel_type = django_filters.ChoiceFilter(
        field_name='wheel_type',
        choices=lambda: CarAnnouncement.objects
            .values_list('wheel_type', 'wheel_type')
            .distinct(),
        label='Тип руля',
        empty_label='Тип руля'
        )
  


    class Meta:
        model = CarAnnouncement
        fields = [
            'mark', 'model', 'generation',
            'body', 'engine_type', 'engine_capacity',
            'transmission', 'drive', 'color',
            'engine_power_gte', 'engine_power_lte',
            'wheel_type', 'exchange', 'registration',
            'custom_clearence', 'urgency', 'region',
            'city', 'car_condition', 'availability',
        ]

