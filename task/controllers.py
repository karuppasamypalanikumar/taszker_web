from .models import (
  Task,
  Project,
  Status
  )
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from django.db import connections
from django.db.models import Q

class AvailableUserViewController():
  def __init__(self,user: User) -> None:
    self.user = user
    
  def display_result(self):
    users = User.objects.filter(
      is_superuser=False
    ).order_by('id')
    return users

class ViewAllProjectViewController():
  def __init__(self,user: User) -> None:
    self.user = user
  
  def display_result(self):
    projects = Project.objects.all().order_by('id')
    return projects

class ViewAllStatusViewController():
  def __init__(self,user: User) -> None:
    self.user = user
  
  def display_result(self):
    status = Status.objects.all().order_by('id')
    return status

class ViewAllTaskController():
  def __init__(self,user: User) -> None:
    self.user = user
  
  def display_result(self):
    tasks = Task.objects.filter(
      Q(author = self.user) |
      Q(assignees = self.user) |
      Q(assigner = self.user)
    ).distinct().order_by('created_date')
    return tasks