from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from .paginations import BookPagination
from .filters import BookFilter
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class BookListAPIView(ListAPIView):
    permission_classes = []
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ["title", "author", "genre", "price"]
    search_fields = [
        "^title",
    ]
    pagination_class = BookPagination
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer


from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated


class BookCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer


from .serializers import PhotoSerializer


class UploadPhotoAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, pk):
        """
        Upload a photo for a given book.

        Parameters:
        pk (int): The ID of the book to which the photo will be uploaded.

        Request Body:
        photo (file): The photo to be uploaded.

        Returns:
        Response: The uploaded photo if successful, or validation errors if the input data is invalid.
        """

        data = request.data.copy()
        data["book"] = pk

        serializer = PhotoSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            photo = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    permission_classes = []

    def get(self, request, pk):
        """
        Get a book by its id.

        Parameters:
        pk (int): The ID of the book to be retrieved.

        Returns:
        Response: The book if found, or a 404 error if not found.

        Notes:
        If the user is authenticated, the book's views count is incremented.
        """
        user = request.user
        book = get_object_or_404(Book, id=pk)
        if user.is_authenticated:
            if not (user in book.views.all()):
                book.views.add(user)
                book.save()
        return Response(BookSerializer(book).data)


class BookUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer


class BookDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer


from rest_framework.pagination import PageNumberPagination


class SearchAPIView(APIView):
    permission_classes = []

    def get(self, request):
        """
        Search for books by title.

        Parameters:
        query (str): The search query.

        Returns:
        Response: The books that match the search query, paginated to 10 per page.

        Notes:
        The search query is case-insensitive.
        """
        query = request.query_params.get("query")
        books = Book.objects.filter(title__icontains=query)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
