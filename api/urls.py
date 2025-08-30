from django.urls import path
from .views import tasks_web_view

urlpatterns = [
    path('tasks-web/', tasks_web_view, name='tasks-web'),
]
