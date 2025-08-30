from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # display user info
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_complete', 'user']
