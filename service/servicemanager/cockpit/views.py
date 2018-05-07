from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index route")

def detail(request, task_id):
    return HttpResponse("Task: %s." % task_id)

def comments(request, task_id):
    response = "You're looking at the comments on task %s."
    return HttpResponse(response % task_id)

def vote(request, task_id):
    return HttpResponse("You're voting on question %s." % question_id)