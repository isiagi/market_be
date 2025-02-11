from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from django.db import models

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get orders where user is either buyer or seller
        return Order.objects.filter(
            models.Q(buyer=user) | models.Q(spare_part__seller=user)
        ).select_related(
            'buyer',
            'spare_part',
            'spare_part__seller'
        ).order_by('-created_at')