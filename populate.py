from api.models import User, Task
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manger.settings')
django.setup()

# Create sample user
user = User.objects.create(username='dany', password='1234')

# Create sample tasks
Task.objects.create(title='Task 1', description='Do something', user=user)
Task.objects.create(title='Task 2', description='Do something else', user=user)

print("Data created successfully!")
