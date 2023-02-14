from django.db import models
from core.models import PostBase

# Create your models here.
class PhotoPost(PostBase):
    camera_selection=(
        ("Sony","Sony"),
        ("Canon","Canon"),
        ("Nikon","Nikon"),
    )
    lens= models.CharField(null=True,blank=True,max_length=100)
    camera = models.CharField(max_length=10,choices=camera_selection)