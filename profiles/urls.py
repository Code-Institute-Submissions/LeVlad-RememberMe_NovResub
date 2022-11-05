from django.urls import path, include
from tasks import views as t_views
from . import views


urlpatterns = [
    path('', views.profiles_index, name='profiles'),
    path('accounts/', include('allauth.urls')),
    path('tasks/', t_views.get_task_list, name='get_task_list'),
    path('tasks/add_task/', t_views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', t_views.edit_task, name='edit_task'),
    path('tasks/toggle/<int:task_id>', t_views.toggle_task, name='toggle_task'),
    path('tasks/delete/<int:task_id>/', t_views.delete_task, name='delete_task'),


]
