from django import forms
from ..models import CarAccessorie, CarAccessoriesImage
from common.forms.multi_file_inp import MultiFileInput


class CarAccessoriesForm(forms.ModelForm):
    class Meta:
        model = CarAccessorie
        exclude = ['created_at', 'updated_at', 'profile']
        fields = ['name', 'profile', 'mark',
                  'model', 'generation', 'price',
                  'region', 'city', 'condition',
                  'availability', 'dscription']
        
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
        

class CarAccessoriesImageForm(forms.ModelForm):
    image = forms.ImageField(widget=MultiFileInput)

    class Meta:
        model = CarAccessoriesImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'}),
            }

