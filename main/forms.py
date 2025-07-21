from django import forms
from .models import Car_announcement

class CarAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Car_announcement
        fields = '__all__'
