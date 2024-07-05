from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #Abstract user already requires username and password, so we just have to add extra fields
    email = models.CharField(max_length=50, unique=True)
    preferred_name = models.CharField(max_length=50)