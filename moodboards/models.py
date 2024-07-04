from django.db import models
from artobjects.models import Artobject

# Create your models here.
class Moodboard(models.Model):
    def __str__(self):
        return f'{self.title}'
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    artobjects = models.ManyToManyField(Artobject, related_name='moodboards', blank=True)
    createdby = models.ForeignKey(
        "jwt_auth.User",
        related_name="moodboards",
        on_delete=models.CASCADE
    )