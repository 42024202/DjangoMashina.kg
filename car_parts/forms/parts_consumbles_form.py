from django import forms
from car_parts.models import PartsAndConsumble, PartsAndConsumblesImage


class PartsAndConsumblesForm(forms.ModelForm):
    class Meta:
        model = PartsAndConsumble
        exclude = ['profile', 'created_at', 'updated_at']
        fields = ['mark', 'model', 'generation',
                 'price', 'region', 'city',
                  'condition', 'availability', 'description',
                  ]
        widgets = {
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
        
class MultiFileInpup(forms.ClearableFileInput):
    allow_multiple_selected = True


class PartsAndConsumblesImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = PartsAndConsumblesImage
        fields = ['image']
        widgets = {
            'image': MultiFileInpup(attrs={'multiple': True, 'class': 'form-control'})
                }


