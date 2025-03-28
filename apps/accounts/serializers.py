from rest_framework.serializers import ModelSerializer, Serializer
from .models import MyUser


from rest_framework.fields import CharField, ValidationError


class RegisterSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = (
            "username",
            "password",
            "confirm_password",
            "email",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise ValidationError("Passwords do not match")
        return data

    def validate_username(self, obj):
        if MyUser.objects.filter(username=obj).exists():
            raise ValidationError("Username already exists")
        return obj

    def create(self, validated_data):
        # Remove confirm_password as it's not needed for user creation
        validated_data.pop("confirm_password", None)

        # Create user with all validated data
        user = MyUser.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(Serializer):
    old_password = CharField(write_only=True)
    new_password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise ValidationError("Passwords do not match")
        return data


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ("username", "email", "first_name", "last_name")
