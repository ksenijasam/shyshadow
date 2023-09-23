from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login_view", views.login_view, name = "login_view"),
    path("register", views.register, name = "register"),
    path("logout_view", views.logout_view, name = "logout_view"),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/<int:id>", views.appointments, name="appointments_with_id"),
    path("diary", views.diary, name="diary"),
    path("diary_entries", views.diary_entries, name="diary_entries"),
    path("goals", views.goals, name="goals"),
]
