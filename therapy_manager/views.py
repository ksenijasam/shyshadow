from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .models import User, Appointment, Diary, Goal

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


@login_required
def appointments(request, id = None):
    clients = User.objects.filter(is_therapist = False)
    appoinments = Appointment.objects.all()

    if request.method == "POST" and id is None:
        appointment = Appointment()

        appointment.status = "new"
        appointment.appointment_date = request.POST["appointment_date"]
        appointment.title = request.POST["title"]
        appointment.client = User.objects.get(username = request.POST["client"])
        appointment.therapist = request.user

        appointment.save()
    elif id:
        appointment = Appointment.objects.get(pk = id)
        appointment.status = 'canceled'

        appointment.save()

        context = {
            'message': 'Successfully canceled appointment'
        }

        return JsonResponse(context, status=200)

    context = {
        'appointments': appoinments,
        'clients': clients
    }

    return render(request, "therapy_manager/appointments.html", context)


@login_required
def diary(request):
    if request.method == 'POST':
        new_diary_entry = Diary()

        new_diary_entry.user = request.user
        new_diary_entry.entry = request.POST["diary_entry"]
        new_diary_entry.entry_date = request.POST["diary_entry_date"]

        new_diary_entry.save()

        return render(request, "therapy_manager/diary.html")
    else:
        return render(request, "therapy_manager/diary.html")

@login_required
def diary_entries(request):
    entries = Diary.objects.filter(user = request.user).order_by('-entry_date') 

    context = {
        'entries': entries
    }

    return render(request, "therapy_manager/diary_entries.html", context)

@login_required
def goals(request): 
    if request.method == 'POST':
        goal = Goal()

        goal.user = request.user
        goal.goal = request.POST["goalText"]

        goal.save()
        
        goals = Goal.objects.filter(user = request.user).order_by('-goal_date') 

        context = {
            'goals': goals
        }

        return render(request, "therapy_manager/goals.html", context)
    else:
        goals = Goal.objects.filter(user = request.user).order_by('-goal_date') 

        context = {
            'goals': goals
        }

        return render(request, "therapy_manager/goals.html", context)


@login_required
def goals_status(request, id): 
    goal = get_object_or_404(Goal, pk=id)

    goal.completed = not goal.completed 

    goal.save()

