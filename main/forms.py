from django import forms
from .models import Car

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        final_attrs = {'multiple': True}
        if attrs:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs)

class CarForm(forms.ModelForm):
    images = forms.FileField(
        widget=MultiFileInput(),
        required=False,
        label='Фотографии'
    )

    class Meta:
        model = Car
        fields = [
            'category', 'mark', 'model', 'year', 'price', 'engine', 'car_condition',
            'region', 'city', 'body', 'color', 'transmission', 'drive', 'wheel_type',
            'exchange', 'registration', 'custom_clearence', 'description', 'is_available', 'is_quickly'
        ]

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data.pop('images', None)  # чтобы не валидировалось моделью
        return cleaned_data

