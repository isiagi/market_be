from rest_framework import viewsets
from .models import SparePart
from .serializers import SparePartSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SparePartFilter

class SparePartViewSet(viewsets.ModelViewSet):
    serializer_class = SparePartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SparePartFilter
    
    def get_queryset(self):
        return SparePart.objects.select_related(
            'seller', 'category', 'subcategory'
        ).all()
