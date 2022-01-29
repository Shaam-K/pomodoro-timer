"""tailwind_project URL Configuration

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
from django.urls import path
from tailwind_app.views import timer,timer_form,timer_task_detail
from tasks.views import tasks,tasks_form,task_database
urlpatterns = [
    path('', timer),
    path('timer/', timer_task_detail),
    path('timer/',timer, name="home"),
    path('timer/start/',timer_form, name="timer_form"),
    path('tasks/', tasks, name="tasks"),
    path('tasks/add', tasks_form, name="task_form"),
    path('tasks/view', task_database, name="view_tasks"),
    path('admin/', admin.site.urls),
]
