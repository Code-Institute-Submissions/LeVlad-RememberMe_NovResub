from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    """
    Function to get the main page
    """
    return render(request, 'home.html')


def get_login(request):
    """
    Function to get the login page
    """
    return render(request, 'login.html')


def get_index(request):
    """
    Function to get the index page
    """
    return render(request, 'index.html')


def get_task_list(request):
    """
    Function to get all the elements and render them in HTML
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)


def add_task(request):
    """
    Function to add a task to the Reminders list by filling a form with
    descriptive information of where, what and if it is done
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('get_task_list')
    form = TaskForm()
    context = {
            'form': form
        }

    return render(request, 'add_task.html', context)


def edit_task(request, task_id):
    """
    Function to edit the items created that
    retrieves the information that was sent
    and populates the form ready to edit
    """

    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('get_task_list')
    form = TaskForm(instance=task)
    context = {
            'form': form
        }

    return render(request, 'edit_task.html', context)


def toggle_task(_request, task_id):
    """
    Function to change between the states of a task
    the user ca change it from done to not done
    """
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect('get_task_list')


def delete_task(_request, task_id):
    """Function to delete the task"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('get_task_list')

#current_l = geolocator.geocode(city)

#m = folium.map(width=300, height=500, location=current_l)