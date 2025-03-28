from django.db import models
from apps.base.models import BaseModel
from apps.books.models import Book
from apps.accounts.models import MyUser


# Create your models here.


class Wishlist(BaseModel):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, related_name="wishlist"
    )
    book = models.ManyToManyField(Book, blank=True, related_name="book_wishlist")

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
