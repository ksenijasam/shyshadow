from django.contrib import admin
from .models import User, Appointment, Diary, Goal

# Register your models here.

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Diary)
admin.site.register(Goal)
