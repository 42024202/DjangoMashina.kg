from .models import (Category, WheelType, Exchange,
YearOfProduction, Color, Registration, CustomClearence,
Body, EngineCapacity, EngineType, Transmission, Drive, CarConfig,
CarAnnouncement, CarImage, Promotion, Tariff
        )
from django import forms


"""Character forms"""
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
        }


class WheelTypeForm(forms.ModelForm):
    class Meta:
        model = WheelType
        fields = ['wheel_type_name']
        widgets = {
            'wheel_type_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class YearOfProductionForm(forms.ModelForm):
    class Meta:
        model = YearOfProduction
        fields = ['year']
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['registration']
        widgets = {
            'registration': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomClearenceForm(forms.ModelForm):
    class Meta:
        model = CustomClearence
        fields = ['custom_clearence']
        widgets = {
            'custom_clearence': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


"""Car_config forms"""
class BodyForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EngineTypeForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EngineCapacityForm(forms.ModelForm):
    class Meta:
        model = EngineCapacity
        fields = ['capacity']
        widgets = {
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }


class TransmissionForm(forms.ModelForm):
    class Meta:
        model = Transmission
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CarConfigForm(forms.ModelForm):
    class Meta:
        model = CarConfig
        fields = [
            'mark', 'model', 'generation',
            'body', 'engine_type', 'engine_capacity',
            'transmission', 'drive'
        ]
        widgets = {
            'mark': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'generation': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Select(attrs={'class': 'form-control'}),
            'engine_type': forms.Select(attrs={'class': 'form-control'}),
            'engine_capacity': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'drive': forms.Select(attrs={'class': 'form-control'}),
        }


"""Car_announcement forms"""
class CarAnnouncementForm(forms.ModelForm):
    class Meta:
        model = CarAnnouncement
        exclude = ['profile', 'created_at', 'updated_at', 'car_config',]
        fields = [
            'profile', 'category', 'car_config', 'color', 'price',
            'engine_power', 'car_mileage', 'wheel_type', 'exchange',
            'registration', 'custom_clearence', 'description',
            'urgency', 'year', 'region',
            'city', 'car_condition', 'availability'
        ]

        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'car_config': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'engine_power': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'car_meleage': forms.NumberInput(attrs={'class': 'form-control'}),
            'wheel_type': forms.Select(attrs={'class': 'form-control'}),
            'exchange': forms.Select(attrs={'class': 'form-control'}),
            'registration': forms.Select(attrs={'class': 'form-control'}),
            'custom_clearence': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'urgency_of_announcencenment': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'car_condition': forms.Select(attrs={'class': 'form-control'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
        }

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }
        image = forms.ImageField(required=False)


class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['name', 'price', 'duration_days']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_days': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['car_announcement', 'tariff', 'start_date', 'end_date']
        widgets = {
            'car_announcement': forms.Select(attrs={'class': 'form-control'}),
            'tariff': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

