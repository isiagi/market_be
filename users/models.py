from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    SELLER_TYPES = [
        ('INDIVIDUAL', 'Individual'),
        ('SHOP', 'Registered Shop')
    ]
    
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPES, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_paid_seller = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # New field

    objects = CustomUserManager()

    def __str__(self):
        if self.username:
            return str(self.username)
        elif self.email:
            return str(self.email)
        return f"User {str(self.id)}"
