from django import forms 


class MultiFileInput(forms.ClearableFileInput):
    """Class for multiple file upload"""
    allow_multiple_selected = True

