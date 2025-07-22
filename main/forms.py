from django import forms
from .models import CarAnnouncement

class CarAnnouncementForm(forms.ModelForm):
    class Meta:
        model = CarAnnouncement
        exclude = ['profile']
        fields = '__all__'
