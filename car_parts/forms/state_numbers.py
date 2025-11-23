from django import forms
from ..models import StateNumber, StateNumberImage
from common.forms.multi_file_inp import MultiFileInput


class StateNumbersForm(forms.ModelForm):
    class Meta:
        model = StateNumber
        exclude = ['profile', 'created_at', 'updated_at']
        fields = ['number', 'price', 'region', 'city', 'description',
                  ]
        widgets = {
                'number':forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'region': forms.Select(attrs={'class': 'form-control'}),
                'city': forms.Select(attrs={'class': 'form-control'}),
                'dscription': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                }
        

class PartsAndConsumblesImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = StateNumberImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'multiple': True, 'class': 'form-control'})
                }

