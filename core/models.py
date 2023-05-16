from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class PostBase(models.Model):
    CATETORIES=(
        ('Blog','Blog'),
        ('Photo','Photo'),
        ('Travel','Travel'),
        ('Review','Review'),
        ('Project','Project'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=7,choices=CATETORIES)
    description = models.CharField(max_length=200)
    post_time = models.DateField()
    thumbnail = models.ImageField(null=True,blank=True,upload_to="images/")

class BaseForm(ModelForm):
    class Meta:
        model = PostBase
        fields = ["title","category","description","thumbnail"]
        labels = {'title': 'title', 
                  'category': 'category',
                  'description': 'description',
                  'thumbnail': 'thumbnail'}
        
        widgets = {
            'thumbnail': forms.ClearableFileInput(attrs={'onchange': 'PreviewImage()'})
        }


