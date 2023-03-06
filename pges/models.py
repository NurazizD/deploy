from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ImageField(upload_to='rasmlar/')
    