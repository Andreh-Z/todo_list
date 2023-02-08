from django.urls import path
from . import views

# list
urlpatterns = [
    path("", views.taskList, name="tasks")
] 