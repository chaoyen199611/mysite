from django.db import models
from django.forms import ModelForm
from django import forms
from .models import PostBase
from blog.models import BlogPost

class BaseForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPost
        fields = ["title","category","description","thumbnail"]
        widgets = {
            'thumbnail': forms.ClearableFileInput(attrs={'onchange': 'PreviewImage()'})
        }
