from ..models import CarAnnouncement, CarImage
from django import forms


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
    image = forms.ImageField(required=False)
    class Meta:
        model = CarImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }

