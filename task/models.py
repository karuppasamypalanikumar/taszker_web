from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comment(models.Model):
  description = models.CharField(
    max_length=500
  )
  created_time = models.DateTimeField()

class Task(models.Model):
  title = models.CharField(
    max_length=100
  )
  description = models.CharField(
    max_length=500
  )
  author = models.ForeignKey(
    to=User,
    on_delete=models.CASCADE,
    related_name="author_user"
  )
  assignees = models.ManyToManyField(
    to=User,
    related_name="assignees_user"
  )
  assigner = models.ForeignKey(
    to=User,
    on_delete=models.SET_NULL,
    null=True,
    related_name="assigner_user"
  )
  created_date = models.DateTimeField()
  updated_date = models.DateTimeField()
  comments = models.ManyToManyField(
    to=Comment,
    related_name="comments_list",
    blank=True
  )
  # attachments in feature release
  
