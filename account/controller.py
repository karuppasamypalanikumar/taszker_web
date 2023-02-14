from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError
from . import serializers
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
        if self.username is None:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": "Username can't be empty"
                },
                code=HTTP_400_BAD_REQUEST
            )
        if self.password is None:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": "Password can't be empty"
                },
                code=HTTP_400_BAD_REQUEST
            )
        username_length = len(self.username)
        if username_length < 6:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": "Username Should be minimum 6 Characters"
                },
                code=HTTP_400_BAD_REQUEST
            )
        password_length = len(self.password)
        if password_length < 8:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": "Password Should be minimum 8 Characters"
                },
                code=HTTP_400_BAD_REQUEST
            )
        # Check for Old User
        if User.objects.filter(username=self.username).exists():
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": "User already present please go to login or Choose a different username"
                },
                code=HTTP_400_BAD_REQUEST
            )

    def __parse__(self):
        data = self.request.data
        self.username = data.get('username')
        self.password = data.get('password')


class SignInController():
    def __init__(self,request:Request) -> None:
        self.request = request
        self.__validate__()
        
    def __validate__(self):
        pass
    
    def display_values(self):
        username = self.request.data.get("username")
        user = User.objects.get(username=username)
        ser = serializers.UserSerializer(
            instance=user
        )
        return ser.data