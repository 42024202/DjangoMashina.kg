from django.contrib import admin
from .models import Category, MarkOfCar, ModelOfCar, YearOfProduction, EngineType, CarCondition, Region, City, BodyType, Color, Transmission, Car, Availability, Drive, WheelType, Exchange, Registration, CustomClearence, CarImage, Quickly, Profile


admin.site.register(Category)
admin.site.register(MarkOfCar)
admin.site.register(ModelOfCar)
admin.site.register(YearOfProduction)
admin.site.register(EngineType)
admin.site.register(CarCondition)
admin.site.register(Region)
admin.site.register(BodyType)
admin.site.register(Color)
admin.site.register(Transmission)
admin.site.register(Availability)
admin.site.register(Drive)
admin.site.register(WheelType)
admin.site.register(Exchange)
admin.site.register(Registration)
admin.site.register(CustomClearence)
admin.site.register(Quickly)
admin.site.register(City)
admin.site.register(Profile)

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1 
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ("id", "mark", "model", "price")
