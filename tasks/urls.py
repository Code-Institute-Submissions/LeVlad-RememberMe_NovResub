from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [

    path('tasks', views.get_task_list, name='task_list'),
    path('tasks/add_task/', views.add_task, name='add'),
    path('edit/<task_id>/', views.edit_task, name='edit_task'),
    path('delete/<task_id>/', views.delete_task, name='delete'),
    ]
