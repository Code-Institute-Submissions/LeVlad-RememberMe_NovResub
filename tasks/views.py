from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def get_task_list(request):
    """
    Function to get all the elements and render them in HTML
    """
    current_user = request.user
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
            }

    tasks.filter(pk=current_user.id)

    return render(request, 'profiles/tasks/task_list.html', context)


def add_task(request):
    """
    Function to add a task to the Reminders list by filling a form with
    descriptive information of where, what and if it is done
    """

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form} added successfully!')
            context = {
                'form': form
                }
            return redirect('get_task_list')
        else:
            messages.error(request,
                           f'Failed to add {form}. Please ensure the form is valid.')
    else:
        form = TaskForm()

        context = {
            'form': form
        }

    return render(request, 'tasks/add_task.html', context)


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
            messages.success(request, f'{form} updated successfully!')

        return redirect('get_task_list')

    form = TaskForm(instance=task)
    context = {
            'form': form
        }
    return render(request, 'tasks/edit_task.html', context)


def toggle_task(request, task_id):
    """
    Function to change between the states of a task
    the user ca change it from done to not done
    """
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    messages.success(request, 'Successfully updated task!')
    return redirect('get_task_list')


def delete_task(request, task_id):
    """Function to delete the task"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task successfully deleted!')
    return redirect('get_task_list')
