from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def profiles_index(request):
    """
    Function to get the profile main page
    """
    return render(request, 'profiles/profiles.html')


