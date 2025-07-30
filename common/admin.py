from django.contrib import admin
from .models import Region, City, Condition, Avalability, Mark, Model, Generation

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "region")
    list_filter = ("region",)

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Avalability)
class AvalabilityAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "mark")
    list_filter = ("mark",)

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ("name", "model")
    list_filter = ("model",)
