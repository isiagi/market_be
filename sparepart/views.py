from rest_framework import viewsets, filters
from .models import SparePart
from .serializers import SparePartSerializer

# Create your views here.
class SparePartViewSet(viewsets.ModelViewSet):
    serializer_class = SparePartSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'make', 'model']
    ordering_fields = ['price', 'created_at']

    
    def get_queryset(self):
        # Get all spare parts
        queryset = SparePart.objects.all()
        
        # Annotate queryset with custom ordering
        queryset = queryset.select_related('seller').order_by(
            '-seller__is_paid_seller',  # Paid sellers first
            '-is_featured',             # Featured items next
            '-created_at'               # Newest items next
        )
        
        return queryset
