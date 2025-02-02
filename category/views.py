from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def subcategories(self, request, slug=None):
        category = self.get_object()
        subcategories = category.subcategories.all()
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data)
