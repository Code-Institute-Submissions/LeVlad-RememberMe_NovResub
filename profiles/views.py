from django.shortcuts import render


def profiles_index(request):
    """
    Function to get the profile main page
    """
    return render(request, 'profiles/profiles.html')
