from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ImageField,
    PrimaryKeyRelatedField,
)
from .models import Book, Photo


class BookSerializer(ModelSerializer):
    views_count = SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "genre",
            "description",
            "image",
            "views_count",
            "price",
        )

    def get_views_count(self, obj):
        """
        Returns the number of users who have viewed this book.
        """
        return obj.views.count()


class PhotoSerializer(ModelSerializer):
    photo = ImageField()
    book = PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Photo
        fields = ("id", "photo", "book")
