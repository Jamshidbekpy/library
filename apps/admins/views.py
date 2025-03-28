from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from apps.accounts.models import MyUser
from .serializers import UserProfileSerializer
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.
class UsersListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = MyUser.objects.all()
    serializer_class = UserProfileSerializer


class DeleteUserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def delete(self, request, pk):
        user = get_object_or_404(MyUser, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class OrdersListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


from .serializers import StatisticSerializer


class StatisticAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        statistic = StatisticSerializer()
        return Response(statistic.data, status=status.HTTP_200_OK)
