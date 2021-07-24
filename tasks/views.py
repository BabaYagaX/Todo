from tasks.models import Task
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
  #1st parameter is request
  #2nd parameter is template_name
  #3rd parameter is context

  tasks =Task.objects.all()

  context = {
    'tasks': tasks
  }

  return render(
    request,
    "home.html",
    context
  )

def addtask (request):
  return render(request,"addtask.html")

def edittask (request):
  return render(request,"edittask.html")
