from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
  title = models.CharField(
      max_length=250
  )
  description = models.CharField(
      max_length=500
  )

  def __str__(self) -> str:
    return self.title


class Comment(models.Model):
  description = models.CharField(
      max_length=500
  )
  created_time = models.DateTimeField()


class Status(models.Model):
  title = models.CharField(
      max_length=50
  )
  created_time = models.DateTimeField()

  def __str__(self) -> str:
    return self.title


class Task(models.Model):

  title = models.CharField(
      max_length=100
  )

  description = models.CharField(
      max_length=500
  )

  status = models.ForeignKey(
      to=Status,
      on_delete=models.SET_NULL,
      null=True,
      related_name="status_name"
  )

  project = models.ForeignKey(
      to=Project,
      on_delete=models.CASCADE,
      related_name="project_name"
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
  last_visited_date = models.DateTimeField()
  updated_date = models.DateTimeField()
  comments = models.ManyToManyField(
      to=Comment,
      related_name="comments_list",
      blank=True
  )
  # attachments in feature release

  def __str__(self) -> str:
    return self.title
