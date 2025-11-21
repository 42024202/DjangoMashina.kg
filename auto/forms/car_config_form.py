from ..models import Body, Drive, EngineType, EngineCapacity, Transmission, CarConfig
from django import forms


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

