from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.TextField()
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    comment = models.TextField()
    visited_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'memories'

class Images(models.Model):
    memory_id = models.ForeignKey(
        Memory,
        on_delete=models.CASCADE
    )
    img_url = models.TextField()