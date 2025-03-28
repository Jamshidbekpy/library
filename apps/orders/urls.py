from rest_framework.urls import path
from .views import (
    OrderCreateAPIView,
    OrdersListAPIView,
    OrderDetailAPIView,
    OrderCancelAPIView,
    OrderHistoryAPIView,
    OrderDeliveryStatusChangeAPIView,
)

urlpatterns = [
    path("create/", OrderCreateAPIView.as_view(), name="create-order"),
    path("orders/", OrdersListAPIView.as_view(), name="orders-list"),
    path("<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("<int:pk>/cancel/", OrderCancelAPIView.as_view(), name="order-cancel"),
    path("history/", OrderHistoryAPIView.as_view(), name="order-history"),
    path(
        "<int:pk>/delivery-status/",
        OrderDeliveryStatusChangeAPIView.as_view(),
        name="order-delivery-status",
    ),
]
