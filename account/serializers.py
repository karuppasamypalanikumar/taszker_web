from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "token"]

    def get_token(self, obj):
        try:
            token = Token.objects.get(
                user=obj
            )
            return str(token)
        except:
            token =  Token.objects.create(user=obj)
            return str(token)
