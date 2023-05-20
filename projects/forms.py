from django.forms import ModelForm
from .models import ProjectPost
from django import forms

class ProjectForm(ModelForm):
    thumbnail = forms.ImageField()
    class Meta:
        model = ProjectPost
        fields = ["topic","just_test"]

        widgets = {
            'thumbnail': forms.ClearableFileInput(attrs={'onchange': 'PreviewImage()'})
        }
