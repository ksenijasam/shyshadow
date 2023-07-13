from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "therapy_manager/index.html", {})

def login(request):
    return render(request, "therapy_manager/login.html", {})
