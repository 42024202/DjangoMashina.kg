from ..models import Promotion, Tariff
from django import forms


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

