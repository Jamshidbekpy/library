from django.db import models
from apps.base.models import BaseModel
from apps.accounts.models import MyUser

# Create your models here.


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="book_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.ManyToManyField(MyUser, blank=True, related_name="viewed_books")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Photo(BaseModel):
    photo = models.ImageField(upload_to="photos/")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_photos")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return f"Photo: {self.photo}"
