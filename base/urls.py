from django.urls import path
from . import views

# list
urlspatterns = [
    path("", views.taskList, name="tasks")
] 