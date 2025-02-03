from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'buyer', 'seller', 'spare_part', 'product_name', 'fullName', 'email', 'phone', 'product_price',
                 'quantity', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['buyer', 'seller', 'product_name', 'product_price']

    def get_seller(self, obj):
        return obj.seller.id

    def get_product_name(self, obj):
        return obj.spare_part.name

    def get_product_price(self, obj):
        return obj.spare_part.price

    def create(self, validated_data):
        validated_data['buyer'] = self.context['request'].user
        return super().create(validated_data)