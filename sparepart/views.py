from rest_framework import viewsets
from .models import SparePart
from .serializers import SparePartSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SparePartFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class SparePartViewSet(viewsets.ModelViewSet):
    serializer_class = SparePartSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SparePartFilter
    
    def get_queryset(self):
        return SparePart.objects.select_related(
            'seller', 'category', 'subcategory'
        ).all()
    
    # seller = current_user
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    # router to get user's own spareparts
    @action(detail=False, methods=['get'])
    def my_spareparts(self, request):
        spareparts = SparePart.objects.filter(seller=self.request.user)
        serializer = SparePartSerializer(spareparts, many=True)
        return Response(serializer.data)
