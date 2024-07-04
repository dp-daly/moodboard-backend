from django.db import models

# Create your models here.
class Artobject(models.Model):
    def __str__(self):
        return f'{self.title}'

    title = models.CharField(blank=True, null=True)
    artist = models.CharField(max_length=70, blank=True, null=True)
    api_object = models.CharField(max_length=300)
    user_text = models.TextField(max_length=1000, blank=True, null=True)
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name = "artobjects",
        on_delete=models.CASCADE
    )

    #may not need owner here, but leaving for now