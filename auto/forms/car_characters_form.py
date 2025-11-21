from django import forms
from ..models import Category, WheelType, Exchange, YearOfProduction, Color, Registration, CustomClearence


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

