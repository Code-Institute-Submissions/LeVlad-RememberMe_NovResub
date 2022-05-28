from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


"""

Function to get all the elements and render them in HTML

"""


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


"""
Function to add an item to the ToDo list by filling a form with
descriptive information of where, what and if it is done
"""


def add_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('get_todo_list')
    form = ItemForm()
    context = {
            'form': form
        }

    return render(request, 'todo/add_item.html', context)


"""
Function to edit the items created
that retrieves the information that was sent 
and populates the form ready to edit
"""


def edit_item(request, item_id):
    
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()

        return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
            'form': form
        }

    return render(request, 'todo/edit_item.html', context)

"""
Function to change between the states of a task
the user ca change it from done to not done
"""


def toggle_item(request, item_id):
    item = get_object_or_404(Item,id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

"""
Function to delete the task
"""


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')