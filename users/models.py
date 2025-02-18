from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    # Override username field to allow alphanumeric, spaces, and special characters
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s]+$',  # Updated regex to allow letters, numbers, and spaces
                message='Username can only contain letters, numbers, and spaces.',
                code='invalid_username'
            ),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    
    SELLER_TYPES = [
        ('INDIVIDUAL', 'Individual'),
        ('SHOP', 'Registered Shop')
    ]
    
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPES, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_address = models.CharField(max_length=200, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_paid_seller = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        if self.username:
            # Strip extra whitespace and normalize spaces
            self.username = ' '.join(self.username.split())

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.username:
            return str(self.username)
        elif self.email:
            return str(self.email)
        return f"User {str(self.id)}"
