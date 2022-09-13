from django.shortcuts import render


def home(request):
    """
    Function to get the main page
    """
    return render(request, 'reminder/home.html')


def index(request):
    """
    Function to get the index page
    """
    return render(request, 'reminder/index.html')


def get_login(request):
    """
    Function to get the login page
    """
    return render(request, 'registration/login.html')
