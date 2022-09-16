from django.urls import path
from reminder import views

urlpatterns = [
    path('reminder', views.get_task_list, name='task_list'),

    ]