from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profiles_index, name='profiles'),
    path('tasks/', include('tasks.urls')),
]
