from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    comments = models.TextField(max_length=255)