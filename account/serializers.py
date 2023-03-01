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
        token = Token.objects.get_or_create(obj)
        return str(token[0])
