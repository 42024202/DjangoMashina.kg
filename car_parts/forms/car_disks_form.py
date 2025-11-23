from django import forms 
from car_parts.models import CarDisk, DiskType, CarDiskImage
from common.forms.multi_file_inp import MultiFileInput


class CarDiskForm(forms.ModelForm):
    class Meta:
        model = CarDisk
        exclude = ['profile', 'created_at', 'updated_at']
        fields = ['disk_type', 'fastener_driling', 'disk_diameter',
                  'mark', 'model', 'generation',
                  'proce', 'year_of_prodction', 'region', 'city',
                  'condition', 'availability', 'description',
                  ]

        widgets = {
                'disk_type': forms.Select(attrs={'class': 'form-control'}),
                'fastener_driling': forms.Select(attrs={'class': 'form-control'}),
                'disk_diameter': forms.Select(attrs={'class': 'form-control'}),
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
        

class DiskTypeForm(forms.ModelForm):
    class Meta:
        model = DiskType
        fields = ['name']
        widgets = {
                "name": forms.Select(attrs={'class': 'form-control'}),
                }

class CarDiskImageForm(forms.ModelForm):
    class Meta:
        model = CarDiskImage
        fields = ['image']
        widgets = {
                "image": MultiFileInput(attrs={'class': 'form-control'}),
                }

