from django.db import models
from apps.base.models import BaseModel
from apps.accounts.models import MyUser
from apps.books.models import Book

# Create your models here.


class Comment(BaseModel):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        MyUser,
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
        blank=True,
    )


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="ratings")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "user"], name="unique_user_book_rating"
            )
        ]
