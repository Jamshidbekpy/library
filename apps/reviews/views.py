from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Comment, Rating
from .serializers import CommentSerializer
from apps.books.models import Book


class CommentListAPIView(APIView):
    permission_classes = []

    def get(self, request, pk):
        return Response(
            CommentSerializer(
                Book.objects.get(id=pk).comments.filter(is_active=True), many=True
            ).data,
            status=status.HTTP_200_OK,
        )


class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteCommentAPIView(APIView):
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        if comment.user == request.user or request.user.is_superuser:
            comment.delete()
            return Response(
                {"message": "Comment deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {"message": "You are not allowed to delete this comment"},
            status=status.HTTP_403_FORBIDDEN,
        )


from .serializers import RatingSerializer


class RateAPIView(APIView):
    def post(self, request, pk):
        user = request.user
        book = Book.objects.get(id=pk)
        rating = request.data.get("rating")
        if rating:
            Rating.objects.create(rating=rating, book=book, user=user)
            return Response(
                RatingSerializer(book.ratings.filter(user=user), many=True).data
            )
        return Response(
            {"message": "Rating is required"}, status=status.HTTP_400_BAD_REQUEST
        )


from django.db.models import Avg
from apps.books.serializers import BookSerializer


class BestBooksAPIView(APIView):
    permission_classes = []

    def get(self, request):
        books = (
            Book.objects.filter(ratings__isnull=False)
            .annotate(avg_rating=Avg("ratings__rating"))
            .order_by("-avg_rating")
        )
        return Response(
            BookSerializer(books, many=True).data, status=status.HTTP_200_OK
        )
