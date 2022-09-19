from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('edit/<task_id>/', views.edit_task, name='edit_task'),
    path('delete/<task_id>/', views.delete_task, name='delete'),
    ]