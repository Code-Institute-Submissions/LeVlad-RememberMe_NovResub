from django.urls import path
from tasks import views as t_views
from . import views


urlpatterns = [
    path('', views.profiles_index, name='profiles'),
    path('tasks/', t_views.get_task_list, name='task_list'),
    path('tasks/add_task/', t_views.add_task, name='add'),
    path('tasks/edit/<int:task_id>/', t_views.edit_task, name='edit'),
    path('tasks/toggle/<int:task_id>', t_views.toggle_task, name='toggle'),
    path('tasks/delete/<int:task_id>/', t_views.delete_task, name='delete'),

]
