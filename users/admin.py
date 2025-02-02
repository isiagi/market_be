from django.contrib import admin

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','last_name', 'first_name', 'email', 'password', 'seller_type', 'business_name', 'contact_phone', 'contact_email', 'address', 'is_paid_seller', 'profile_image')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'seller_type', 'business_name', 'contact_phone', 'contact_email', 'address', 'is_paid_seller', 'profile_image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'seller_type', 'business_name', 'contact_phone', 'contact_email', 'address', 'is_paid_seller', 'profile_image'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
