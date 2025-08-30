from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model (optional, or use default User)
class User(AbstractUser):
    pass  # we can expand later if needed

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
