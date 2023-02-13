from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)


# Create your views here.
class SignInView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class SignUpView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class VerifyEmailView(APIView):
    def get(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )

    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class ChangePasswordView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )


class DeleteAccountView(APIView):
    def post(self, request: Request):
        return Response(
            data={},
            status=HTTP_200_OK
        )
