from django.shortcuts import render, redirect
from .models import Item



def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):


    if request.method == "POST":
        name = request.POST.get("item_name")
        location = request.POST.get("item_location")
        priority = request.POST.get("item_priority")
        done = "done" in request.POST
        Item.objects.create(
            name=name, location=location, priority=priority, done=done
            )

        return redirect('get_todo_list')

    return render(request, 'todo/add_item.html')