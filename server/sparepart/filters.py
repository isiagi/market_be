import django_filters
from .models import SparePart
from django.db import models
from category.models import Category

class SparePartFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(method='filter_year_range')
    year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    market = django_filters.CharFilter(field_name='seller__market')
    make = django_filters.CharFilter(field_name='make', lookup_expr='iexact')
    model = django_filters.CharFilter(field_name='model', lookup_expr='icontains')
    category = django_filters.CharFilter(method='filter_category')
    subcategory = django_filters.CharFilter(field_name='subcategory__slug', 
                                          lookup_expr='exact')
    condition = django_filters.ChoiceFilter(choices=SparePart.CONDITIONS)
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    def filter_year_range(self, queryset, name, value):
        return queryset.filter(
            models.Q(year__lte=value, year_end__gte=value) |
            models.Q(year=value)
        )
    
    def filter_category(self, queryset, name, value):
        try:
            category = Category.objects.get(slug=value)
            return queryset.filter(
                models.Q(category=category) |
                models.Q(category__parent=category)
            )
        except Category.DoesNotExist:
            return queryset.none()
    
    class Meta:
        model = SparePart
        fields = ['year', 'market', 'make', 'model', 'category', 
                 'subcategory', 'condition']