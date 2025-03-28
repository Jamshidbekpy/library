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
from .models import Wishlist
from apps.books.models import Book
from .serializers import WishlistSerializer

# Create your views here.


class WishlistListView(ListAPIView):
    queryset = Wishlist.objects.filter(is_active=True)
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class WishlistAddBookAPIView(APIView):
    def post(self, request, pk):
        """
        Wishlistga kitob qo'shish uchun POST requesti

        Parameters:
        book_id (int): Wishlistga qo'shish kerak bo'lgan kitobning id'si

        Returns:
        JSON response with a message about the result of the operation
        """
        user = request.user

        try:
            book = Book.objects.filter(is_active=True).get(id=pk)
        except Book.DoesNotExist:
            return Response(
                {"error": "Kitob topilmadi"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            wishlist = Wishlist.objects.get(user=user)
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(user=user)

        if book in wishlist.book.all():
            return Response(
                {"message": "Kitob wishlistda bor"}, status=status.HTTP_400_BAD_REQUEST
            )

        wishlist.book.add(book)
        return Response(
            {"message": "Kitob wishlistga qo'shildi"}, status=status.HTTP_200_OK
        )


class WishlistRemoveBookAPIView(APIView):
    def post(self, request, pk):
        user = request.user

        try:
            book = Book.objects.filter(is_active=True).get(id=pk)
        except Book.DoesNotExist:
            return Response(
                {"error": "Kitob topilmadi"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            wishlist = Wishlist.objects.get(user=user)
        except Wishlist.DoesNotExist:
            return Response(
                {"error": "Wishlist topilmadi"}, status=status.HTTP_404_NOT_FOUND
            )

        wishlist.book.remove(book)
        return Response(
            {"message": "Kitob wishlistdan o'chirildi"}, status=status.HTTP_200_OK
        )
