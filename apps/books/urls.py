from rest_framework.urls import path
from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,
    UploadPhotoAPIView,
    SearchAPIView,
)

urlpatterns = [
    path("", BookListAPIView.as_view(), name="book-list"),
    path("<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),
    path("create/", BookCreateAPIView.as_view(), name="book-create"),
    path("<int:pk>/update/", BookUpdateAPIView.as_view(), name="book-update"),
    path("<int:pk>/delete/", BookDeleteAPIView.as_view(), name="book-delete"),
    path("<int:pk>/upload-photo/", UploadPhotoAPIView.as_view(), name="upload-photo"),
    path("search/", SearchAPIView.as_view(), name="search"),
]
