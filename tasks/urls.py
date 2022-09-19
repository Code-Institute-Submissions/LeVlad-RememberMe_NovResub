from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('list/', views.get_task_list, name='list'),
    path('add/', views.add_task, name='add'),
    path('edit/<task_id>/', views.edit_task, name='edit_task'),
    path('delete/<task_id>/', views.delete_task, name='delete'),
    ]