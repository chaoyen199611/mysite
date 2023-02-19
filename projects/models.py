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

class ProjectPostSection(models.Model):
    belongPost = models.ForeignKey(ProjectPost,on_delete=models.CASCADE)
    section_num = models.IntegerField(null=True)
    section_title = models.CharField(null=True,blank=True,max_length=100)
    section_context = models.TextField(null=True,blank=True)
    section_image = models.ImageField(null=True,blank=True,upload_to="images/projects/")