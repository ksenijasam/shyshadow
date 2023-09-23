from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name =  models.CharField(max_length = 20)
    surname =  models.CharField(max_length = 30)
    is_therapist = models.BooleanField(default = False)


class Appointment(models.Model):
    NEW = 'new'
    CANCELED = 'canceled'
    DONE = 'done'
    CATEGORY_CHOICES = [
        (NEW, 'new'),
        (CANCELED, 'canceled'),
        (DONE, 'done'),
    ]

    status = models.CharField(choices=CATEGORY_CHOICES, null=True, blank=True, max_length=10)
    appointment_date = models.DateTimeField(auto_now_add = False, null = True)
    title = models.CharField(max_length=50)
    comment = models.TextField()
    client = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name = 'client_appointment')
    therapist = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name = 'therapist_appointment')

    def __str__(self):
        return f"{self.client} has appointment {self.appointment_date} with {self.therapist}, status {self.status}"


class  Diary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name = 'user_diary')
    entry =  models.TextField()
    entry_date = models.DateTimeField(auto_now_add = False, null = True)

    def __str__(self):
        return f"{self.user} has added diary entry on {self.entry_date}"


class  Goal(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name = 'user_goal')
    goal =  models.TextField()
    goal_date = models.DateTimeField(auto_now_add = False, null = True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user} has added goal on {self.goal_date}"