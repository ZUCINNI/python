"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.views.generic.edit import FormView
from django.contrib import messages

def welcome(request):
    """Renders the welcome page."""
    return render(request, 'registration/welcome.html')

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('welcome')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'registration/registration.html', {'form': f})