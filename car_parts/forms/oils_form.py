from django import forms
from ..models import CarOil, CarOilsImage
from common.forms.multi_file_inp import MultiFileInput


class CarOilForm(forms.ModelForm):
    class Meta:
        model = CarOil
        exclude = ['profile', 'created_at', 'updated_at']
        fields = ['name', 'mark', 'model', 'generation',
                 'price', 'region', 'city',
                 'condition', 'availability', 'description',
                  ]
        widgets = {
                'name':forms.TextInput(attrs={'class': 'form-control'}),
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
        model = CarOilsImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'})
                }

