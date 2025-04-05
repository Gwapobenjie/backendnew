from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

def home(request):
    return render(request, 'home.html')

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
