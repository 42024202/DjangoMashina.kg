from django.contrib import admin
from .models import Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, EngineCapacity, EnginePower, CarCondition, Region, City,BodyType, ColorOfCar, CarMeleage, Transmission, CarAnnouncement, Availability,Drive, WheelType, Exchange, Registration, CustomClearence, CarImage, Profile


simple_models = [
   Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, EngineCapacity, EnginePower, CarCondition, Region, BodyType, ColorOfCar, Transmission, Availability, Drive, WheelType, Exchange, Registration, CustomClearence, City, Profile,  
        ]
for model in simple_models:
    admin.site.register(model)


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1 
@admin.register(CarAnnouncement)


class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ("id", "mark", "model", "price")
