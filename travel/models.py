from django.db import models
from core.models import PostBase

# Create your models here.
class TravelPost(PostBase):
    location=models.CharField(max_length=100)
    country=models.CharField(max_length=100)