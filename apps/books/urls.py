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

# Documentation

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version="v1",
        description="API lar",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jamshidbekshodibekov2004@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
