from django.contrib import admin

# Register your models here.
from .models import Book, Photo

admin.site.register(Book)
admin.site.register(Photo)
