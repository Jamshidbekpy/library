from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    price_book = serializers.SerializerMethodField()
    price_all = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "book",
            "status",
            "delivery_status",
            "is_paid",
            "price_book",
            "price_all",
            "quantity",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "user": {"read_only": True},
            "is_paid": {"read_only": True},
            "status": {"read_only": True},
            "delivery_status": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def get_price_book(self, obj):
        return obj.book.price

    def get_price_all(self, obj):
        return obj.book.price * obj.quantity

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["book"] = instance.book.title
        representation["user"] = instance.user.username
        return representation
