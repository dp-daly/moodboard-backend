from django.db import models
from moodboards.models import Moodboard

# Create your models here.
class Artobject(models.Model):
    def __str__(self):
        return f'{self.title}'

    moodboard = models.ForeignKey(Moodboard, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    artist = models.CharField(max_length=70, blank=True, null=True)
    img = models.CharField(max_length=150, blank=True, null=True)