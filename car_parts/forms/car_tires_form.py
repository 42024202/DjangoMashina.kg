from django import forms
from ..models import CarTire, TireType, CarTireImage
from common.forms.multi_file_inp import MultiFileInput


class TireTypeForm(forms.ModelForm):
    class Meta:
        model = TireType
        fields = ['tire_type']
        widgets = {
                'tire_type': forms.Select(attrs={'class': 'form-control'}),
                }

class CarTiresForm(forms.ModelForm):
    class Meta:
        model = CarTire
        exclude = ['profile', 'created_at', 'updated_at']
        fields = ['car_tire_type', 'tire_width', 'tire_height', 'tire_size',
                  'mark', 'model', 'generation',
                 'price', 'region', 'city',
                  'condition', 'availability', 'description',
                  ]
        widgets = {
                'car_tire_type': forms.Select(attrs={'class': 'form-control'}),
                'tire_width': forms.Select(attrs={'class': 'form-control'}),
                'tire_height': forms.Select(attrs={'class': 'form-control'}),
                'tire_size': forms.Select(attrs={'class': 'form-control'}),
                'mark': forms.Select(attrs={'class': 'form-control'}),
                'model': forms.Select(attrs={'class': 'form-control'}),
                'generation': forms.Select(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'region': forms.Select(attrs={'class': 'form-control'}),
                'city': forms.Select(attrs={'class': 'form-control'}),
                'condition': forms.Select(attrs={'class': 'form-control'}),
                'availability': forms.Select(attrs={'class': 'form-control'}),
                'dscription': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                }
        

class PartsAndConsumblesImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = CarTireImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'})
                }

