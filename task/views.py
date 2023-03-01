from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Task
from . import controllers
from .serializers import (
    TaskSerializer,
    UserSerializer,
    StatusSerializer,
    ProjectSerializer
)
from rest_framework.status import (
    HTTP_200_OK
)


class CreateTaskView(APIView):
    def post(self, request: Request):
        controller = controllers.CreateTaskViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class DeleteTaskView(APIView):
    def delete(self, request: Request):
        controller = controllers.DeleteTaskViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class UpdateTaskView(APIView):
    def post(self, request: Request):
        controller = controllers.UpdateTaskViewController(
            request=request
        )
        return Response(
            data=controller.display(),
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
        controller = controllers.CreateProjectViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class DeleteProjectView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request: Request):
        controller = controllers.DeleteProjectViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class UpdateProjectView(APIView):
    def post(self, request: Request):
        controller = controllers.UpdateProjectViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class CreateStatusView(APIView):
    def post(self, request: Request):
        controller = controllers.CreateStatusViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )


class DeleteStatusView(APIView):
    def delete(self, request: Request):
        controller = controllers.DeleteStatusViewController(
            request=request
        )
        return Response(
            data=controller.display(),
            status=HTTP_200_OK
        )
