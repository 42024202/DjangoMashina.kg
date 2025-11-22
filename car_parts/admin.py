from django.contrib import admin
from .models.parts_and_consumbles import PartsAndConsumble, PartsAndConsumblesImage
from .models.car_disks import DiskType, CarDisk, CarDiskImage
from .models.accessories import CarAccessorie, CarAccessoriesImage
from .models.oils import CarOil, CarOilsImage
from .models.car_for_parts import CarForPart, CarForPartImage
from .models.state_numbers import StateNumber, StateNumberImage
from .models.car_tires import TireType, CarTire, CarTireImage


"""Parts and Consumbles"""
class PartsAndConsumblesImageInline(admin.TabularInline):
    model = PartsAndConsumblesImage
    extra = 1 
    min_num = 0
    max_num = 10


@admin.register(PartsAndConsumble)
class PartsAndConsumbleAdmin(admin.ModelAdmin):
    list_display = ['profile', 'mark', 'model', 'price', 'created_at']
    list_filter = ['mark', 'model', 'profile']
    search_fields = ['mark', 'model']
    ordering = ['-id', 'created_at']
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


@admin.register(CarDisk)
class CarDiskAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'fastener_driling', 'price', 'created_at']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id', 'created_at']
    inlines = [CarDiskImageInline]


"""Car accessories"""
class CarAccessoriesImageInline(admin.TabularInline):
    model = CarAccessoriesImage
    extra = 1
    min_num = 0
    max_num = 10

@admin.register(CarAccessorie)
class CarAccessorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price', 'created_at']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id', 'created_at']
    inlines = [CarAccessoriesImageInline]


"""Oils"""
class CarOilsImageInline(admin.TabularInline):
    model = CarOilsImage
    extra = 1
    min_num = 0
    max_num = 10


@admin.register(CarOil)
class CarOilAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price', 'created_at']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id', 'created_at']
    inlines = [CarOilsImageInline]


"""Car for parts"""
class CarForPartImageInline(admin.TabularInline):
    model = CarForPartImage
    extra = 1
    min_num = 0
    max_num = 10


@admin.register(CarForPart)
class CarForPartAdmin(admin.ModelAdmin):
    list_display = ['profile', 'mark', 'model', 'price', 'city', 'created_at']
    search_fields = ['mark', 'model', 'city']
    ordering = ['-id', 'created_at']


"""State numbers"""
class StateNumberImageInline(admin.TabularInline):
    model = StateNumberImage
    extra = 1
    min_num = 0
    max_num = 10


@admin.register(StateNumber)
class StateNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'number', 'price', 'created_at']
    search_fields = ['id', 'number']
    ordering = ['-id', 'created_at']
    inlines = [StateNumberImageInline]


"""Car tires"""
class CarTireImageInline(admin.TabularInline):
    model = CarTireImage
    extra = 1
    min_num = 0
    max_num = 10


@admin.register(CarTire)
class CarTireAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'car_tire_type', 'tire_size', 'price', 'created_at']
    search_fields = ['id', 'car_tire_type', 'tire_size']
    ordering = ['-id', 'created_at']
    inlines = [CarTireImageInline]


@admin.register(TireType)
class TireTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tire_type']
