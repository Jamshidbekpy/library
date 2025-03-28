from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Order
from .serializers import OrderSerializer


class OrderCreateAPIView(APIView):
    def post(self, request):
        user = request.user
        data = request.data.copy()
        data["user"] = user.id

        if "book" not in data:
            return Response(
                {"book": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Q


class OrdersListAPIView(APIView):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(
            Q(user=user)
            & (
                Q(is_paid=False)
                | Q(delivery_status="on_the_way")
                | Q(delivery_status="at_location")
            )
        )
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailAPIView(APIView):
    def get(self, request, pk):
        user = request.user
        order = get_object_or_404(Order, id=pk, user=user)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderCancelAPIView(APIView):
    def post(self, request, pk):
        user = request.user
        if user.orders.filter(id=pk).exists():
            order = get_object_or_404(Order, id=pk)
            order.status = "cancelled"
            order.save()
            return Response({"message": "Order cancelled"}, status=status.HTTP_200_OK)
        return Response(
            {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
        )


from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated


class OrderDeliveryStatusChangeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        data = request.data.get("delivery_status")
        if data not in ["at_location", "on_the_way", "delivered"]:
            return Response(
                {"message": "Invalid delivery status"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.delivery_status = data
        order.save()
        return Response(
            {"message": "Order delivery status changed"}, status=status.HTTP_200_OK
        )


class OrderHistoryAPIView(APIView):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
