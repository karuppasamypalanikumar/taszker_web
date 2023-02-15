from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)

class Common():
    def __init__(self) -> None:
        print("")
    
    @staticmethod
    def is_none(value,msg):
        if value is None:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": msg
                },
                code=HTTP_400_BAD_REQUEST
            )
    @staticmethod
    def is_length_statisfied(value,required_length,msg):
        actual_length = len(value)
        if actual_length < required_length:
            raise ValidationError(
                detail={
                    "status_code": 0,
                    "status_message": msg
                },
                code=HTTP_400_BAD_REQUEST
            )
            
class UsernameValidator():
    def __init__(self, username, is_need=False) -> None:
        self.username = username
        self.is_need = is_need
        self.__validate__()

    def __validate__(self):
        Common.is_none(
            value=self.username,
            msg="Username can't be empty"
            )
        Common.is_length_statisfied(
            value=self.username,
            required_length=6,
            msg="Username Should be minimum 6 Characters"
        )
        # Check for Old User
        if self.is_need:
            if User.objects.filter(username=self.username).exists():
                raise ValidationError(
                    detail={
                        "status_code": 0,
                        "status_message": "User already present please go to login or Choose a different username"
                    },
                    code=HTTP_400_BAD_REQUEST
                )


class PasswordValidator():
    def __init__(self, username, password, check_pass=False) -> None:
        self.username = username
        self.password = password
        self.check_pass = check_pass
        self.__validate__()

    def __validate__(self):
        Common.is_none(
            value=self.password,
            msg="Password can't be empty"
            )
        Common.is_length_statisfied(
            value=self.password,
            required_length=6,
            msg="Password Should be minimum 8 Characters"
        )
        if self.check_pass:
            if not User.objects.filter(username=self.username,
                                       password=self.password).exists():
                raise ValidationError(
                    detail={
                        "status_code": 0,
                        "status_message": "Please check your password or username"
                    },
                    code=HTTP_400_BAD_REQUEST
                )
