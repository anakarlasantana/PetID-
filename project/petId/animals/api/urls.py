from rest_framework.routers import DefaultRouter
from .views import TemplateViewSet, RGRequestViewSet

router = DefaultRouter()

# Registre as viewsets no roteador
router.register(r'templates', TemplateViewSet, basename='template')
router.register(r'rg', RGRequestViewSet, basename='rg-request')
