from rest_framework.views import (APIView)
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Task
from .serializers import TaskSerializer
from . import controllers
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)


class CreateView(APIView):
  def post(self, request: Request):
    return Response(
        data={},
        status=HTTP_200_OK
    )


class DeleteView(APIView):
  def delete(self, request: Request):
    return Response(
        data={},
        status=HTTP_200_OK
    )


class AssignView(APIView):
  def post(self, request: Request):
    return Response(
        data={},
        status=HTTP_200_OK
    )


class ViewAllView(ListAPIView):
  def get_queryset(self):
    user = self.request.user
    controller = controllers.ViewAllController(
        user=user
    )
    return controller.display_result()

  def get_serializer_class(self):
    return TaskSerializer
