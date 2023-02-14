from django.db import models
from core.models import PostBase

# Create your models here.
class ProjectPost(PostBase):
    differentField=(
        ("Machine Learning","Machine Learning"),
        ("BlockChain ","BlockChain"),
        ("3D Art","3D Art"),
    )
    topic = models.CharField(max_length=20,choices=differentField)
    just_test = models.CharField(null=True,blank=True,max_length=100)