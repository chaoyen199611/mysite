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
    description = models.TextField(null=True,blank=True, default='default')
    post_time = models.DateField()
    thumbnail = models.ImageField(null=True,blank=True,upload_to="images/")


        


