from django.contrib import admin
from .models.parts_and_consumbles import PartsAndConsumble, PartsAndConsumblesImage
from .models.car_disks import DiskType, CarDisk, CarDiskImage
from .models.accessories import CarAccessorie, CarAccessoriesImage
from .models.oils import CarOil, CarOilsImage
from .models.car_for_parts import CarForPart, CarForPartImage
from .models.state_numbers import StateNumber, StateNumberImage
from .models.car_tires import TireType, CarTire, CarTireImage


"""===Base classes==="""
class BaseImageInline(admin.TabularInline):
    extra = 1
    min_num = 0
    max_num = 10


class BaseItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price', 'created_at']
    search_fields = ['mark', 'model']
    ordering = ['-id', 'created_at']
    inlines = []


"""Parts and Consumbles"""
class PartsAndConsumblesImageInline(BaseImageInline):
    model = PartsAndConsumblesImage


@admin.register(PartsAndConsumble)
class PartsAndConsumbleAdmin(BaseItemAdmin):
    list_display = ['profile', 'mark', 'model', 'price', 'created_at']
    list_filter = ['mark', 'model', 'profile']
    inlines = [PartsAndConsumblesImageInline]


"""Car disks"""
class CarDiskImageInline(admin.TabularInline):
    model = CarDiskImage
    extra = 1
    min_num = 0
    max_num = 10

@admin.register(DiskType)
class DiskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['-id']


class CarDiskAdmin(BaseItemAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'fastener_driling', 'price', 'created_at']
    search_fields = ['id', 'mark', 'model']
    inlines = [CarDiskImageInline]


"""Car accessories"""
class CarAccessoriesImageInline(BaseImageInline):
    model = CarAccessoriesImage


@admin.register(CarAccessorie)
class CarAccessorieAdmin(BaseItemAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price', 'created_at']
    inlines = [CarAccessoriesImageInline]


"""Oils"""
class CarOilsImageInline(BaseImageInline):
    model = CarOilsImage


@admin.register(CarOil)
class CarOilAdmin(BaseItemAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price', 'created_at']
    inlines = [CarOilsImageInline]

"""Car for parts"""
class CarForPartImageInline(BaseImageInline):
    model = CarForPartImage


@admin.register(CarForPart)
class CarForPartAdmin(BaseItemAdmin):
    list_display = ['profile', 'mark', 'model', 'price', 'city', 'created_at']
    search_fields = ['mark', 'model', 'city']
    inlines = [CarForPartImageInline]


"""State numbers"""
class StateNumberImageInline(BaseImageInline):
    model = StateNumberImage


@admin.register(StateNumber)
class StateNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'number', 'price', 'created_at']
    search_fields = ['id', 'number']
    ordering = ['-id', 'created_at']
    inlines = [StateNumberImageInline]


"""Car tires"""
class CarTireImageInline(BaseImageInline):
    model = CarTireImage


@admin.register(CarTire)
class CarTireAdmin(BaseItemAdmin):
    list_display = ['id', 'profile', 'car_tire_type', 'tire_size', 'price', 'created_at']
    search_fields = ['id', 'car_tire_type', 'tire_size']
    inlines = [CarTireImageInline]

@admin.register(TireType)
class TireTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tire_type']

