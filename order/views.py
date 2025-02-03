from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Get orders buyer
    def get_queryset(self):
        return self.queryset.filter(buyer=self.request.user)
