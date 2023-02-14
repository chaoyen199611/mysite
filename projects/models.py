from django.db import models
from core.models import PostBase

# Create your models here.
class ProjectPost(PostBase):
    Field=(
        ("Machine Learning","Machine Learning"),
        ("BlockChain ","BlockChain"),
        ("3D Art","3D Art"),
    )
    field = models.CharField(max_length=20,choices=Field)
    just_test = models.CharField(null=True,max_length=100)