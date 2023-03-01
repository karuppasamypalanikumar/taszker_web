from .models import (
    Task,
    Project,
    Status,
    Comment
)
from rest_framework.request import Request
from .serializers import (
    TaskSerializer,
    ProjectSerializer,
    StatusSerializer,
    CommentSerializer
)
from rest_framework.serializers import ValidationError
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from . import validators


class CreateTaskViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.task_title = data.get('task_title')
    self.task_description = data.get('task_description')
    self.status_id = data.get('status_id')
    self.project_id = data.get('project_id')
    self.author = self.request.user
    self.assignees_ids = data.get('assignees_ids')
    self.assigner_id = data.get('assigner_id')
    self.updated_time = timezone.now()
    self.created_time = timezone.now()
    self.last_visited_time = timezone.now()
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.string_validate(
        input=self.task_title,
        msg="Task Title Can't be Empty or Wrong Data Type"
    )
    if self.task_description:
      validators.FormatValidator.string_validate(
          input=self.task_title,
          msg="Task Description Can't be Empty or Wrong Data Type"
      )
    if self.status_id:
      validators.FormatValidator.int_validate(
          input=self.status_id,
          msg="Status id Can't be Empty or Wrong Data Type"
      )
    if self.project_id:
      validators.FormatValidator.int_validate(
          input=self.project_id,
          msg="Project id Can't be Empty or Wrong Data Type"
      )
    if self.assignees_ids:
      validators.FormatValidator.list_validate(
          input=self.assignees_ids,
          msg="Assignees Can't be Empty or Wrong Data Type"
      )
    if self.assigner_id:
      validators.FormatValidator.int_validate(
          input=self.assigner_id,
          msg="Assigner Can't be Empty or Wrong Data Type"
      )
    self.__create_task__()

  def __create_task__(self):
    self.task = Task(
        title=self.task_title
    )
    self.__save_task__()

  def __save_task__(self):
    if self.task_title:
      self.task.title = self.task_title

    if self.task_description:
      self.task.description = self.task_description
    if self.author:
      self.task.author = self.author
    if self.status_id:
      try:
        self.status = Status.objects.get(pk=self.status_id)
        self.task.status = self.status
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid status id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.project_id:
      try:
        self.project = Project.objects.get(pk=self.project_id)
        self.task.project = self.project
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid project id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.assignees_ids:
      try:
        self.assignees = User.objects.filter(
            pk__in=self.assignees_ids).exclude().order_by('id')[:10]
        self.task.assignees = self.assignees
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid assignees ids'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.assigner_id:
      try:
        self.assigner = User.objects.get(pk=self.assigner_id)
        self.task.assigner = self.assigner
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid assigner id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.updated_time:
      self.task.updated_date = self.updated_time
    if self.created_time:
      self.task.created_date = self.created_time
    if self.last_visited_time:
      self.task.last_visited_date = self.last_visited_time
    try:
      self.task.save()
    except:
      raise ValidationError(
          detail={
              'status_code': 0,
              'status_message': 'Missing Required Parameters'
          }
      )

  def display(self):
    serializer = TaskSerializer(
        instance=self.task
    )
    return {
        'status_code': 1,
        'status_message': 'Task Updated Successfully',
        'data': serializer.data
    }


class UpdateTaskViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.task_id = data.get('task_id')
    self.task_title = data.get('task_title')
    self.task_description = data.get('task_description')
    self.status_id = data.get('status_id')
    self.project_id = data.get('project_id')
    self.author = self.request.user
    self.assignees_ids = data.get('assignees_ids')
    self.assigner_id = data.get('assigner_id')
    self.updated_time = timezone.now()
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.task_id,
        msg="Task ID Can't be Empty or Wrong Data Type"
    )
    update_need = False
    if self.task_title:
      update_need = True
      validators.FormatValidator.string_validate(
          input=self.task_title,
          msg="Task Title Can't be Empty or Wrong Data Type"
      )
    if self.task_description:
      update_need = True
      validators.FormatValidator.string_validate(
          input=self.task_title,
          msg="Task Description Can't be Empty or Wrong Data Type"
      )
    if self.status_id:
      update_need = True
      validators.FormatValidator.int_validate(
          input=self.status_id,
          msg="Status id Can't be Empty or Wrong Data Type"
      )
    if self.project_id:
      update_need = True
      validators.FormatValidator.int_validate(
          input=self.project_id,
          msg="Project id Can't be Empty or Wrong Data Type"
      )
    if self.assignees_ids:
      update_need = True
      validators.FormatValidator.list_validate(
          input=self.assignees_ids,
          msg="Assignees Can't be Empty or Wrong Data Type"
      )
    if self.assigner_id:
      update_need = True
      validators.FormatValidator.int_validate(
          input=self.assigner_id,
          msg="Assigner Can't be Empty or Wrong Data Type"
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
      self.task = Task.objects.get(
          pk=self.task_id
      )
      self.__update_data__()
    except:
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": "Invalid task id"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __update_data__(self):
    save_need = False
    if self.task_title:
      self.task.title = self.task_title
      save_need = True

    if self.task_description:
      self.task.description = self.task_description
      save_need = True

    if self.status_id:
      try:
        self.status = Status.objects.get(pk=self.status_id)
        self.task.status = self.status
        save_need = True
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid status id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.project_id:
      try:
        self.project = Project.objects.get(pk=self.project_id)
        self.task.project = self.project
        save_need = True
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid project id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.assignees_ids:
      try:
        self.assignees = User.objects.filter(
            pk__in=self.assignees_ids).exclude().order_by('id')[:10]
        self.task.assignees = self.assignees
        save_need = True
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid assignees ids'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.assigner_id:
      try:
        self.assigner = User.objects.get(pk=self.assigner_id)
        self.task.assigner = self.assigner
        save_need = True
      except:
        raise ValidationError(
            detail={
                'status_code': 0,
                'status_message': 'invalid assigner id'
            },
            code=HTTP_400_BAD_REQUEST
        )
    if self.updated_time:
      self.task.updated_date = self.updated_time
      save_need = True

    if save_need:
      self.task.save()

  def display(self):
    serializer = TaskSerializer(
        instance=self.task
    )
    return {
        'status_code': 1,
        'status_message': 'Task Updated Successfully',
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


class DeleteTaskViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.task_id = data.get('task_id')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.task_id,
        msg="Status ID Can't be Empty or Wrong Data Type"
    )
    self.__fetch_data__()

  def __fetch_data__(self):
    try:
      self.task = Task.objects.get(
          pk=self.task_id
      )
      self.__delete_data__()
    except:
      raise ValidationError(
          detail={
              "status_code": 0,
              "status_message": "Invalid task id"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def __delete_data__(self):
    self.task.delete()

  def display(self):
    return {
        'status_code': 1,
        'status_message': 'Task Deleted Successfully'
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


class AddCommentViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.decription = data.get('decription')
    self.task_id = data.get('task_id')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.task_id,
        msg="Task ID Can't be Empty or Wrong Data Type"
    )
    validators.FormatValidator.string_validate(
        input=self.decription,
        msg="Comment Decription Can't be Empty or Wrong Data Type"
    )
    self.__save__()

  def __save__(self):
    self.comment = Comment(
        decription=self.decription,
        created_time=timezone.now()
    )
    self.comment.save()
    try:
      self.task = Task.objects.get(pk=self.task_id)
      self.task.comments.add(self.comment)
      self.task.save()
    except:
      raise ValidationError(
          detail={
              'status_code': 0,
              'status_message': "Invalid Task ID or Something Went Wrong"
          },
          code=HTTP_400_BAD_REQUEST
      )

  def display(self):
    serializer = CommentSerializer(
        instance=self.comment
    )
    return {
        'status_code': 1,
        'status_message': 'Comment Added Successfully',
        'data': serializer.data
    }


class UpdateCommentViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.comment_id = data.get('comment_id')
    self.decription = data.get('decription')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.comment_id,
        msg="Comment ID Can't be Empty or Wrong Data Type"
    )
    validators.FormatValidator.string_validate(
        input=self.decription,
        msg="Title Can't be Empty or Wrong Data Type"
    )
    self.__save__()

  def __save__(self):
    try:
      self.comment = Comment.objects.get(pk=self.comment_id)
      self.comment.save()
    except:
      raise ValidationError(
          detail={
              'status_code': 0,
              'status_message': 'Invalid Comment ID'
          },
          code=HTTP_400_BAD_REQUEST
      )

  def display(self):
    serializer = CommentSerializer(
        instance=self.comment
    )
    return {
        'status_code': 1,
        'status_message': 'Comment Updated Successfully',
        'data': serializer.data
    }


class DeleteCommentViewController():
  def __init__(self, request: Request) -> None:
    self.request = request
    self.__parse__()

  def __parse__(self):
    data = self.request.data
    self.comment_id = data.get('comment_id')
    self.__validate__()

  def __validate__(self):
    validators.FormatValidator.int_validate(
        input=self.comment_id,
        msg="Comment ID Can't be Empty or Wrong Data Type"
    )
    self.__delete_detail__()

  def __delete_detail__(self):
    try:
      self.comment = Comment.objects.get(pk=self.comment_id)
      self.comment.delete()
    except:
      raise ValidationError(
          detail={
              'status_code': 0,
              'status_message': 'Invalid Comment ID'
          },
          code=HTTP_400_BAD_REQUEST
      )

  def display(self):
    return {
        'status_code': 1,
        'status_message': 'Comment Deleted Successfully',
    }
