from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login.html")
