from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Task
from . import controllers
from .serializers import (
    TaskSerializer,
    UserSerializer,
    StatusSerializer,
    ProjectSerializer
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)


class CreateTaskView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class DeleteTaskView(APIView):
    def delete(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class UpdateTaskView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class ViewAllTaskView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        controller = controllers.ViewAllTaskController(
            user=user
        )
        return controller.display_result()

    def get_serializer_class(self):
        return TaskSerializer


class ViewAllProjectView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        controller = controllers.ViewAllProjectViewController(
            user=user
        )
        return controller.display_result()

    def get_serializer_class(self):
        return ProjectSerializer


class ViewAllStatusView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        controller = controllers.ViewAllStatusViewController(
            user=user
        )
        return controller.display_result()

    def get_serializer_class(self):
        return StatusSerializer


class AvailableUserView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        controller = controllers.AvailableUserViewController(
            user=user
        )
        return controller.display_result()

    def get_serializer_class(self):
        return UserSerializer


class CreateProjectView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class DeleteProjectView(APIView):
    def delete(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class UpdateProjectView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class CreateStatusView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class DeleteStatusView(APIView):
    def delete(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )
