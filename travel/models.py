from django.db import models
from core.models import PostBase

# Create your models here.
class TravelPost(PostBase):
    location=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

class TravelPostSection(models.Model):
    belongPost = models.ForeignKey(TravelPost,on_delete=models.CASCADE)
    section_num = models.IntegerField(null=True)
    section_title = models.CharField(null=True,blank=True,max_length=100)
    section_context = models.TextField(null=True,blank=True)
    section_image = models.ImageField(null=True,blank=True,upload_to="images/travels/")