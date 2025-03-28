from rest_framework.urls import path
from .views import (
    UsersListAPIView,
    DeleteUserAPIView,
    OrdersListAPIView,
    StatisticAPIView,
)

urlpatterns = [
    path("users/", UsersListAPIView.as_view(), name="users-list"),
    path("delete-user/<int:pk>/", DeleteUserAPIView.as_view(), name="delete-user"),
    path("orders/", OrdersListAPIView.as_view(), name="orders-list"),
    path("statistic/", StatisticAPIView.as_view(), name="statistic"),
]
