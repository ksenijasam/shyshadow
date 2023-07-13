from django.db import models

# Create your models here.

class User(models.Model):
    username =  models.CharField(max_length = 20)
    name =  models.CharField(max_length = 20)
    name =  models.CharField(max_length = 30)
    is_therapist = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True, null = True)


    def __str__(self):
        return f"{self.name} {self.surname}, is therapist: {self.is_therapist}"