from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    product_image = serializers.ImageField(source='spare_part.images.first.image', read_only=True)
    seller_name = serializers.CharField(source='seller.business_name', read_only=True)
    seller_contact_phone = serializers.CharField(source='seller.contact_phone', read_only=True)
    seller_contact_email = serializers.CharField(source='seller.contact_email', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'buyer', 'seller', 'spare_part', 'product_name', 'seller_name','product_image', 'seller_contact_phone', 'seller_contact_email', 'fullName', 'email', 'phone', 'product_price',
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