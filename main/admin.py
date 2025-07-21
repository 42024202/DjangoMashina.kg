from django.contrib import admin
from .models import Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, EngineCapacity, EnginePower, CarCondition, Region, City,BodyType, ColorOfCar, CarMeleage, Transmission, Car_announcement, Availability,Drive, WheelType, Exchange, Registration, CustomClearence, CarImage, Profile


admin.site.register(Category)
admin.site.register(MarkOfCar)
admin.site.register(ModelOfCar)
admin.site.register(YearOfProduction)
admin.site.register(EngineType)
admin.site.register(EngineCapacity)
admin.site.register(EnginePower)
admin.site.register(CarCondition)
admin.site.register(Region)
admin.site.register(BodyType)
admin.site.register(ColorOfCar)
admin.site.register(CarMeleage)
admin.site.register(Transmission)
admin.site.register(Availability)
admin.site.register(Drive)
admin.site.register(WheelType)
admin.site.register(Exchange)
admin.site.register(Registration)
admin.site.register(CustomClearence)
admin.site.register(City)
admin.site.register(Profile)

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1 
@admin.register(Car_announcement)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ("id", "mark", "model", "price")
