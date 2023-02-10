from django.db import models

# Create your models here.
class Memory(models.Model):
    location = models.TextField()
    comment = models.TextField()
    img_url = models.TextField()