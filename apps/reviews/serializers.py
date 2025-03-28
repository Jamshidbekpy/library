from .models import Comment, Rating
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CurrentUserDefault,
)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "book", "user")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.username
        return representation


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ("rating", "book", "user")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.username
        return representation
