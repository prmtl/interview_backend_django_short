from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


# NOTE: it is implemented as a separate view as requested, but it could also be a "DELETE" method on a single order view
# right now it is a little bit RPC-ish in style since it is a POST on a "deactivate" path
class DeactivateOrderView(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        order = self.get_object()
        # NOTE: mimics UpdateMixin but we provide our own data, not from request
        serializer = self.get_serializer(order, data={"is_active": False}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
