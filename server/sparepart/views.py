from rest_framework import viewsets
from .models import SparePart
from .serializers import SparePartSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SparePartFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser

class SparePartViewSet(viewsets.ModelViewSet):
    serializer_class = SparePartSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SparePartFilter
    
    def get_queryset(self):
        return SparePart.objects.select_related(
            'seller', 'category', 'subcategory'
        ).prefetch_related('images').all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    @action(detail=False, methods=['get'])
    def my_spareparts(self, request):
        spareparts = SparePart.objects.filter(seller=self.request.user)
        # Use self.get_serializer to ensure proper context is passed
        serializer = self.get_serializer(spareparts, many=True)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)