from rest_framework.serializers import ModelSerializer
from .models import Wishlist


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("user", "book", "created_at")
