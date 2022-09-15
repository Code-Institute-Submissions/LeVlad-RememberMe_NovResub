from django.urls import path
from . import views

urlpatterns = [
    path('reminder/', views.get_reminder_list, name='reminder_list'),
    path('/add/', views.add_task, name='add'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle'),
    path('edit/<int:task_id>', views.toggle_task, name='edit'),
    path('delete/<int:task_id>', views.delete_task, name='delete'),
    ]