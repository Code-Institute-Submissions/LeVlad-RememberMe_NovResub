"""rememberme2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks import views
from reminder import views as view_r
from home import views as view_h
from tasks import views as view_t


urlpatterns = [
    path('admin', admin.site.urls),
    path('', view_h.home, name='home'),
    path('reminder', view_r.get_index, name='index'),
    path('accounts', include('allauth.urls')),
    path('profiles', include('profiles.urls')),
    path('add', view_t.add_task, name='add'),
    path('toggle/<int:task_id>', view_t.toggle_task, name='toggle'),
    path('edit/<int:task_id>', view_t.toggle_task, name='edit'),
    path('delete/<int:task_id>', view_t.delete_task, name='delete'),
    path('reminder', views.get_task_list, name='get_task_list'),
    ]
