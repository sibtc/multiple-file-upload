from django import forms
from .models import PhotoModel

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('file', )
