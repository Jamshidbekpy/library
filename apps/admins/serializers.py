from rest_framework.serializers import (
    ModelSerializer,
)
from apps.accounts.models import MyUser


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ("username", "email", "first_name", "last_name")
