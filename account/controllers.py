from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ValidationError
from . import serializers
from . import validaters
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)


class SignUpController():

    def __init__(self, request: Request) -> None:
        self.request = request
        self.__parse__()
        self.__validate_details__()
        self.__create_user_model__()

    def __create_user_model__(self):
        self.user = User(
            username=self.username,
            password=self.password,
            is_superuser=False,
            is_active=True
        )
        # Saving User
        self.user.save()

    def display_details(self):
        serializer = serializers.UserSerializer(
            instance=self.user,
            many=False
        )
        return serializer.data

    def __validate_details__(self):
        # Validate User name
        # min username length 6
        validaters.UsernameValidator(
            username=self.username,
            is_need=True
        )
        validaters.PasswordValidator(
            username=self.username,
            password=self.password,
            check_pass=False
        )

    def __parse__(self):
        data = self.request.data
        self.username = data.get('username')
        self.password = data.get('password')


class SignInController():
    def __init__(self, request: Request) -> None:
        self.request = request
        self.__parse__()

    def __validate_details__(self):
        validaters.UsernameValidator(
            username=self.username,
            is_need=False
        )
        validaters.PasswordValidator(
            username=self.username,
            password=self.password,
            check_pass=True
        )

    def display_values(self):
        username = self.request.data.get("username")
        user = User.objects.get(username=username)
        ser = serializers.UserSerializer(
            instance=user,
            many=False
        )
        return ser.data

    def __parse__(self):
        data = self.request.data
        self.username = data.get('username')
        self.password = data.get('password')
        self.__validate_details__()


class SignOutController():
    def __init__(self, request: Request) -> None:
        self.request = request

    def __logout_user__(self):
        pass
