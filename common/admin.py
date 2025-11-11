from django.contrib import admin
from .models import Region, City, Condition, Availability, Mark, Model, Generation, MotoSeries

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', "name")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "region")
    list_filter = ("region",)

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', "name")

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "mark")
    list_filter = ("mark",)

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ("name", "model")
    list_filter = ("model",)


@admin.register(MotoSeries)
class MotoSeriesAdmin(admin.ModelAdmin):
    list_display = ("series",)
    search_fields = ("series",)

