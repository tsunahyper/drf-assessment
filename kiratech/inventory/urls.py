from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventory.views import InventoryViewSet, InventoryListView, InventoryDetailView

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    # Template views
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('detail/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    
    # API views
    path('', include(router.urls)),
]
