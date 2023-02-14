from django.db import models


# Create your models here.

class PostBase(models.Model):
    CATETORIES=(
        ('B','Blog'),
        ('P','Photo'),
        ('T','Travel'),
        ('R','Review'),
        ('Pr','Project'),
    )
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=2,choices=CATETORIES)
    description = models.CharField(max_length=100)
    post_time = models.DateTimeField(auto_now_add=True)