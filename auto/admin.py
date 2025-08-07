from django.contrib import admin
from .models import (
    CarAnnouncement, CarImage, Category, WheelType, Exchange,
    YearOfProduction, Color, Registration, CustomClearence, Body,
    EngineType, EngineCapacity, Transmission, Drive, CarConfig,
    Promotion, Tariff
)


@admin.register(CarAnnouncement)
class CarAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'category', 'price', 'created_at', 'updated_at', 'urgency')
    list_filter = ('category', 'created_at', 'urgency')
    search_fields = ('profile__user__username', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    inlines = []

class PromotionInline(admin.TabularInline):
    model = Promotion
    extra = 0
    readonly_fields = ('start_date', 'end_date')
    verbose_name_plural = 'Продвижения'

# Inline для CarImage под CarAnnouncement
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

CarAnnouncementAdmin.inlines = [CarImageInline]


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_days')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('car_announcement', 'tariff', 'start_date', 'end_date', 'is_active')
    list_filter = ('tariff', 'start_date', 'end_date')

    @admin.display(boolean=True, description='Активен?')
    def is_active(self, obj):
        return obj.is_active()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

@admin.register(WheelType)
class WheelTypeAdmin(admin.ModelAdmin):
    list_display = ('wheel_type_name',)

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(YearOfProduction)
class YearOfProductionAdmin(admin.ModelAdmin):
    list_display = ('year',)
    ordering = ('-year',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration',)

@admin.register(CustomClearence)
class CustomClearenceAdmin(admin.ModelAdmin):
    list_display = ('custom_clearence',)

@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EngineCapacity)
class EngineCapacityAdmin(admin.ModelAdmin):
    list_display = ('capacity',)

@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Drive)
class DriveAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CarConfig)
class CarConfigAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'generation', 'body', 'engine_type', 'engine_capacity', 'transmission', 'drive')
    search_fields = ('mark__name', 'model__name')

