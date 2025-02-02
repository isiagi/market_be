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

    # Get only the top-level categories
    @action(detail=False, methods=['get'])
    def top_categories(self, request):
        top_categories = Category.objects.filter(parent=None)
        serializer = CategorySerializer(top_categories, many=True)
        return Response(serializer.data)
    
    # Get all subcategories from all categories
    @action(detail=False, methods=['get'])
    def all_subcategories(self, request):
        subcategories = Category.objects.filter(parent__isnull=False)
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def subcategories(self, request, slug=None):
        category = self.get_object()
        subcategories = category.subcategories.all()
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data)
