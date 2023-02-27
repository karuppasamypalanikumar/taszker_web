from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from django.db import connections
from django.db.models import Q

class ViewAllController():
  def __init__(self,user: User) -> None:
    self.user = user
  
  def display_result(self):
    tasks = Task.objects.filter(
      Q(author = self.user) |
      Q(assignees = self.user) |
      Q(assigner = self.user)
    ).distinct().order_by('created_date')
    return tasks