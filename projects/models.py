from django.db import models
from core.models import PostBase


class ProjectPost(PostBase):
    model = models.ForeignKey('ProjectPost', on_delete=models.CASCADE)
    differentField=(
        ("Machine Learning","Machine Learning"),
        ("BlockChain ","BlockChain"),
        ("3D Art","3D Art"),
    )
    topic = models.CharField(max_length=20,choices=differentField)
    image = models.ImageField(null=True,blank=True,upload_to='images/projects/')
    maincontent = models.TextField(null=True,blank=True, default='default') 

