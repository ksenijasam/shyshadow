from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name =  models.CharField(max_length = 20)
    surname =  models.CharField(max_length = 30)
    is_therapist = models.BooleanField(default = False)

