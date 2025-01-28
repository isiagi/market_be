from django.db import models
from users.models import CustomUser as User
from sparepart.models import SparePart
from django.core.validators import MinValueValidator

# Create your models here.
class Order(models.Model):
    """Order model for spare parts"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
