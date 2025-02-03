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
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.spare_part.name}"
    
    @property
    def seller(self):
        return self.spare_part.seller
