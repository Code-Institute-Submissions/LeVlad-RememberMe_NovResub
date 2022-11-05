from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


@login_required
def profiles_index(request):
    """
    Function to get the profile main page
    """
    return render(request, 'profiles/profiles.html')
