from django.db import models
from django.core.validators import MinValueValidator
from users.models import CustomUser as Profile
from category.models import Category


class SparePart(models.Model):
    """Spare parts product model"""
    CONDITIONS = [
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('REFURBISHED', 'Refurbished')
    ]

    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='parts', null=True, blank=True)
    subcategory = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                  related_name='subparts', null=True, blank=True)
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITIONS)
    
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-seller__is_paid_seller', '-is_featured', '-created_at']