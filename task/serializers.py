from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Task,
    Project,
    Status
)


class UserSerializer(serializers.ModelSerializer):
  name = serializers.SerializerMethodField()

  class Meta:
      model = User
      fields = ['id', 'name']

  def get_name(self, obj):
    return obj.first_name + " " + obj.last_name


class TaskSerializer(serializers.ModelSerializer):
  title = serializers.CharField()
  description = serializers.CharField()
  author = UserSerializer()
  created_date = serializers.DateTimeField()

  class Meta:
    model = Task
    fields = ['title', 'description', 'author', 'created_date']


class ProjectSerializer(serializers.ModelSerializer):
  title = serializers.CharField()
  description = serializers.CharField()

  class Meta:
    model = Project
    fields = ['id', 'title', 'description']


class StatusSerializer(serializers.ModelSerializer):
  title = serializers.CharField()

  class Meta:
    model = Status
    fields = ['id', 'title']
