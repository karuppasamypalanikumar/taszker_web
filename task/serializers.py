from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
  name = serializers.SerializerMethodField()
  
  class Meta:
        model = User
        fields = ['name']

  def get_name(self, obj):
    return obj.first_name + " " + obj.last_name

class TaskSerializer(serializers.ModelSerializer):
  title = serializers.CharField()
  description = serializers.CharField()
  author = UserSerializer()

  class Meta:
    model = Task
    fields = ['title','description','author']
    
