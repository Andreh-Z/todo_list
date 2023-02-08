from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# function to view

def taskList(requests):
        return HttpResponse("To Do List")