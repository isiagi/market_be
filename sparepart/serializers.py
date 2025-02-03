from rest_framework import serializers
from .models import SparePart

class SparePartSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.business_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = SparePart
        fields = ['id', 'seller', 'seller_name', 'category', 'category_name',
                 'subcategory', 'subcategory_name', 'name', 'description',
                 'make', 'model', 'year', 'year_end', 'condition',
                 'stock_quantity', 'price', 'is_featured', 'created_at']


    # check seller seller_type is SHOP
    def validate_seller(self, value):
        if value.seller_type != 'SHOP':
            raise serializers.ValidationError('Seller type must be SHOP')
        return value 