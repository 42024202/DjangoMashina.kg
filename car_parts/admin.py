from django.contrib import admin
from .models.parts_and_consumbles import PartsAndConsumble, PartsAndConsumblesImage
from .models.car_disks import DiskType, CarDisk, WheelImage
from .models.accessories import CarAccessorie, CarAccessoriesImage
from .models.oils import CarOil, CarOilsImage
from .models.car_for_parts import CarForPart, CarForPartImage
from .models.state_numbers import StateNumber, StateNumberImage
from .models.car_tires import TireType, CarTire


@admin.register(PartsAndConsumble)
class PartsAndConsumbleAdmin(admin.ModelAdmin):
    list_display = ['profile', 'mark', 'model', 'price']
    list_filter = ['mark', 'model', 'profile']
    search_fields = ['mark', 'model']
    ordering = ['-id']


@admin.register(DiskType)
class DiskTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['-id']


@admin.register(CarDisk)
class CarDiskAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'fastener_driling', 'price']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id']


@admin.register(CarAccessorie)
class CarAccessorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id']


@admin.register(CarOil)
class CarOilAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'mark', 'model', 'price']
    search_fields = ['id', 'mark', 'model']
    ordering = ['-id']


@admin.register(CarForPart)
class CarForPartAdmin(admin.ModelAdmin):
    list_display = ['profile', 'mark', 'model', 'price', 'city']
    search_fields = ['mark', 'model', 'city']
    ordering = ['-id']


@admin.register(StateNumber)
class StateNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'number', 'price']
    search_fields = ['id', 'number']
    ordering = ['-id']


