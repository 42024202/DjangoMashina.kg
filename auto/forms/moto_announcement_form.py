from ..models import MotoAnnouncement, MotoAnnouncementImage
from django import forms 


class MotoAnnouncementForm(forms.ModelForm):
    class Meta:
        model = MotoAnnouncement
        exclude = ['profile', 'created_at']
        fields = ['type_of_moto', 'mark', 'model', 'series',
                  'year_of_production', 'car_mileage', 'color',
                  'price', 'condition', 'availability',
                  'region', 'city', 'exchange',
                  'registration', 'custom_clearence', 'urgency', 'description'
                  ]
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'type_of_moto': forms.Select(attrs={'class': 'form-control'}),
            'mark': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'series': forms.Select(attrs={'class': 'form-control'}),
            'year_of_production': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'car_meleage': forms.NumberInput(attrs={'class': 'form-control'}),
            'exchange': forms.Select(attrs={'class': 'form-control'}),
            'registration': forms.Select(attrs={'class': 'form-control'}),
            'custom_clearence': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
        }


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MotoImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = MotoAnnouncementImage
        fields = ['image']
        widgets = {
                'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'})
        }

