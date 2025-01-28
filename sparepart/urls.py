from rest_framework import routers
from .views import SparePartViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('sparepart', SparePartViewSet, basename='sparepart')

urlpatterns = [
    path('', include(router.urls)),
]