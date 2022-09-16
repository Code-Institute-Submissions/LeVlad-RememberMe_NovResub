from django.shortcuts import render


def home(request):
    """
    Function to get the main page
    """
    return render(request, 'home.html')
