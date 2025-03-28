from rest_framework.urls import path

from .views import (
    CommentListAPIView,
    CreateCommentAPIView,
    DeleteCommentAPIView,
    RateAPIView,
    BestBooksAPIView,
)

urlpatterns = [
    path("<int:pk>/comments/", CommentListAPIView.as_view(), name="comment-list"),
    path("comments/create/", CreateCommentAPIView.as_view(), name="comment-create"),
    path(
        "comment/<int:pk>/delete/",
        DeleteCommentAPIView.as_view(),
        name="comment-delete",
    ),
    path("<int:pk>/rate/", RateAPIView.as_view(), name="rate"),
    path("best-books/", BestBooksAPIView.as_view(), name="best-books"),
]
