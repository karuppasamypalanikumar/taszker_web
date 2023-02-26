from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import controllers
from .paginations import StandardPagination
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


class ViewAllView(APIView):
  permission_classes = [AllowAny]
  pagination_class = StandardPagination
  def get(self, request: Request):
    controller = controllers.ViewAllController()
    return Response(
        data=controller.display_result(),
        status=HTTP_200_OK
    )
