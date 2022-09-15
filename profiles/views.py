from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def profiles_index(request):
    """
    Function to get the profile main page
    """
    return render(request, 'profiles/profile.html')

@login_required()
def profile(request):
    """
    Function to get the profile via login
    """
    return render(request, 'profiles/profile.html')    
