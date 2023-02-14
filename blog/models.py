from django.db import models
from core.models import PostBase

# Create your models here.
class BlogPost(PostBase):
    text = models.TextField(null=True)
    just_test = models.CharField(null=True,max_length=100)