from django.shortcuts import render


def get_login(request):
    """
    Function to get the login page
    """
    return render(request, 'login.html')


def get_index(request):
    """
    Function to get the index page
    """
    return render(request, 'templates/index.html')


def handler404(request, *args, **kwargs):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)
