from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User

# Create your views here.

def index(request):
    return render(request, "therapy_manager/index.html", {})

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "therapy_manager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "therapy_manager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        name = request.POST["name"]
        surname = request.POST["surname"]
        is_therapist = request.POST.get("therapist", False) == "true"

        if password != confirmation:
            return render(request, "therapy_manager/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username = username, email = email, password = password, name = name, surname = surname, is_therapist = is_therapist)
            user.save()
        except IntegrityError:
            return render(request, "therapy_manager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "therapy_manager/register.html")


def appointments(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "therapy_manager/appointments.html")
    
