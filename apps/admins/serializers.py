from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
)
from apps.books.models import Book
from apps.accounts.models import MyUser


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ("username", "email", "first_name", "last_name")


from apps.orders.models import Order
from django.db.models import Sum


class StatisticSerializer(Serializer):
    user_count = SerializerMethodField()
    sold_books_price = SerializerMethodField()

    class Meta:
        fields = ("user_count", "sold_books_price")

    def get_user_count(self, obj):
        return MyUser.objects.count()

    def get_sold_books_price(self, obj):
        return Order.objects.filter(is_paid=False).aggregate(total_price=Sum("price"))
