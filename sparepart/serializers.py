from rest_framework import serializers
from django.conf import settings
from .models import SparePart, SparePartImage

class SparePartImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SparePartImage
        fields = ['id', 'spare_part', 'image']

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                # Ensure we're using the full URL including scheme and domain
                return request.build_absolute_uri(obj.image.url)
            return f"{settings.MEDIA_URL}{obj.image}"
        return None

class SparePartSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.business_name', read_only=True)
    seller_contact = serializers.CharField(source='seller.contact_phone', read_only=True)
    seller_address = serializers.CharField(source='seller.business_address', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    images = SparePartImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = SparePart
        fields = ['id', 'seller', 'seller_name', 'category', 'category_name',
                 'subcategory', 'subcategory_name', 'name', 'description', 'seller_contact', 'seller_address',
                 'make', 'model', 'year', 'year_end', 'condition', 'images', 'uploaded_images',
                 'stock_quantity', 'price', 'is_featured', 'created_at']

    def validate_seller(self, value):
        if value.seller_type != 'SHOP':
            raise serializers.ValidationError('Seller type must be SHOP')
        return value 

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images', [])
        spare_part = SparePart.objects.create(**validated_data)
        
        for image_data in images_data:
            SparePartImage.objects.create(spare_part=spare_part, image=image_data)
        
        return spare_part