from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator


class SparePart(models.Model):
    """Spare parts product model"""
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Additional flags for paid version sellers
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Added for sorting

    class Meta:
        ordering = ['-seller__is_paid_seller', '-is_featured', '-created_at']  # Priority ordering