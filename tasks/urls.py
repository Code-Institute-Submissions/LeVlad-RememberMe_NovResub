from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [

    path('', views.get_task_list, name='task_list'),
    path('add_task/', views.add_task, name='add'),
    path('edit/<task_id>/', views.edit_task, name='edit'),
    path('toggle/<task_id>', views.toggle_task, name='toggle'),
    path('delete/<task_id>/', views.delete_task, name='delete'),
    ]
