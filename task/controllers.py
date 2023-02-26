from .models import Task
from .serializers import TaskSerializer

class ViewAllController():
  def __init__(self) -> None:
    pass
  
  def __validate__(self):
    pass
  
  def display_result(self):
    tasks = Task.objects.all()
    serializer = TaskSerializer(
      instance=tasks,
      many=True
    )
    return serializer.data