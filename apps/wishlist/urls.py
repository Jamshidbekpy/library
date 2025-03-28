from django.urls import path
from .views import WishlistListView, WishlistAddBookAPIView, WishlistRemoveBookAPIView

urlpatterns = [
    path("list/", WishlistListView.as_view(), name="wishlist-list"),
    path(
        "add-book/<int:pk>", WishlistAddBookAPIView.as_view(), name="wishlist-add-book"
    ),
    path(
        "remove-book/<int:pk>",
        WishlistRemoveBookAPIView.as_view(),
        name="wishlist-remove-book",
    ),
]
