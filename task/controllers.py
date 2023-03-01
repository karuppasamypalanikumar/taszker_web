from .models import (
    Task,
    Project,
    Status
)
from rest_framework.request import Request
from .serializers import (
    TaskSerializer,
    ProjectSerializer,
    StatusSerializer
)
from rest_framework.serializers import ValidationError
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connections
from django.db.models import Q
from . import validators


class CreateTaskViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__verify_result__()

  def __verify_result__(self):
    # Title
    self.title = self.request.data.get('title')
    self.__save_details__()

  def __save_details__(self):
    self.task = Task(

    )
    self.task.save()

  def display_message(self):
    serializer = TaskSerializer(
        instance=self.task
    )
    return {
        'status_code': 1,
        'status_message': 'Task Created Sucessfully',
        'data': serializer.data
    }


class CreateProjectViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()
    self.__validate__()

  def __parse__(self):
    data = self.request.data
    self.title = data.get('title')
    self.description = data.get('description')

  def __validate__(self):
    validators.FormatValidator.string_validate(
        input=self.title,
        msg="Title Can't be Empty or Wrong Data Type"
    )
    validators.FormatValidator.string_validate(
        input=self.description,
        msg="Description Can't be Empty or Wrong Data Type"
    )
    self.__save__()

  def __save__(self):
    self.project = Project(
        title=self.title,
        description=self.description
    )
    self.project.save()

  def display(self):
    serializer = ProjectSerializer(
        instance=self.project
    )
    return {
        'status_code': 1,
        'status_message': 'Project Created Successfully',
        'data': serializer.data
    }


class CreateStatusViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()
    self.__validate__()

  def __parse__(self):
    data = self.request.data
    self.title = data.get('title')

  def __validate__(self):
    validators.FormatValidator.string_validate(
        input=self.title,
        msg="Title Can't be Empty or Wrong Data Type"
    )
    self.__save__()

  def __save__(self):
    self.status = Status(
        title=self.title,
        created_time=timezone.now()
    )
    self.status.save()

  def display(self):
    serializer = StatusSerializer(
        instance=self.status
    )
    return {
        'status_code': 1,
        'status_message': 'Status Created Successfully',
        'data': serializer.data
    }


class DeleteStatusViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.status_id = data.get('status_id')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.status_id,
        msg="Status ID Can't be Empty or Wrong Data Type"
    )
    self.__fetch_data__()

  def __fetch_data__(self):
    try:
      self.status = Status.objects.get(
          pk=self.status_id
      )
      self.__delete_data__()
    except:
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": "Invalid status id"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __delete_data__(self):
    self.status.delete()

  def display(self):
    return {
        'status_code': 1,
        'status_message': 'Status Deleted Successfully'
    }


class DeleteProjectViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.project_id = data.get('project_id')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.project_id,
        msg="Project ID Can't be Empty or Wrong Data Type"
    )
    self.__fetch_data__()

  def __fetch_data__(self):
    try:
      self.project = Project.objects.get(
          pk=self.project_id
      )
      self.__delete_data__()
    except:
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": "Invalid project id"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __delete_data__(self):
    self.project.delete()

  def display(self):
    return {
        'status_code': 1,
        'status_message': 'Project Deleted Successfully'
    }


class AvailableUserViewController():
  def __init__(self, user: User) -> None:
    self.user = user

  def display_result(self):
    users = User.objects.filter(
        is_superuser=False
    ).order_by('id')
    return users


class ViewAllProjectViewController():
  def __init__(self, user: User) -> None:
    self.user = user

  def display_result(self):
    projects = Project.objects.all().order_by('id')
    return projects


class ViewAllStatusViewController():
  def __init__(self, user: User) -> None:
    self.user = user

  def display_result(self):
    status = Status.objects.all().order_by('id')
    return status


class ViewAllTaskController():
  def __init__(self, user: User) -> None:
    self.user = user

  def display_result(self):
    tasks = Task.objects.filter(
        Q(author=self.user) |
        Q(assignees=self.user) |
        Q(assigner=self.user)
    ).distinct().order_by('created_date')
    return tasks


class UpdateProjectViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.project_id = data.get('project_id')
    self.project_title = data.get('project_title')
    self.project_description = data.get('project_description')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.project_id,
        msg="Project ID Can't be Empty or Wrong Data Type"
    )
    update_need = False
    if self.project_title:
      update_need = True
      validators.FormatValidator.string_validate(
          input=self.project_title,
          msg="Title Can't be Empty or Wrong Data Type"
      )
    if self.project_description:
      update_need = True
      validators.FormatValidator.string_validate(
          input=self.project_title,
          msg="Description Can't be Empty or Wrong Data Type"
      )
    if update_need:
      self.__fetch_data__()
    else:
      raise ValidationError(
          detail={
              'status_code': 0,
              'status_message': 'No Valid Detail To Update'
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __fetch_data__(self):
    try:
      self.project = Project.objects.get(
          pk=self.project_id
      )
      self.__update_data__()
    except:
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": "Invalid project id"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __update_data__(self):
    self.project.title = self.project_title
    self.project.save()

  def display(self):
    return {
        'status_code': 1,
        'status_message': 'Project Updated Successfully'
    }
