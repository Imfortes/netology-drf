# advertisements/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet

router = DefaultRouter()
router.register('', AdvertisementViewSet, basename='advertisements')

urlpatterns = router.urls