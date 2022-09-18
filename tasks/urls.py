from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_task_list, name='task_list'),
    path('add/', views.add_task, name='add'),
    path('edit/<task_id>/', views.edit_task, name='edit'),
    path('delete/<task_id>/', views.delete_task, name='delete'),
    ]