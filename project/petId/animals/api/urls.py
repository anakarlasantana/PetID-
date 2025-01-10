from rest_framework.routers import DefaultRouter
from .views import TemplateViewSet, RGRequestViewSet

router = DefaultRouter()

router.register(r'templates', TemplateViewSet, basename='template')
router.register(r'rg', RGRequestViewSet, basename='rg-request')
