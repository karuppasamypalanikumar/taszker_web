from django.contrib import admin
from .models import Task, Comment
# Register your models here.

admin.site.register(
  model_or_iterable= [
    Task,Comment
  ]
)