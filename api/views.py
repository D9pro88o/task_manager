from .models import Task, User
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from django.shortcuts import render
from .models import Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def tasks_web_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_web.html', {'tasks': tasks})