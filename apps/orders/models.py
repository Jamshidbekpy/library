from django.db import models
from apps.base.models import BaseModel
from apps.books.models import Book
from apps.accounts.models import MyUser


# Create your models here.
class Order(BaseModel):

    DELIVERY_CHOICES = (
        ("at_location", "Avval joyida"),
        ("on_the_way", "Yo‘lda"),
        ("delivered", "Yetkazildi"),
    )
    STATUS = (
        ("active", "Aktiv"),
        ("cancelled", "Bekor qilindi"),
    )
    status = models.CharField(max_length=20, choices=STATUS, default="active")
    delivery_status = models.CharField(
        max_length=20, choices=DELIVERY_CHOICES, default="at_location"
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="orders")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
