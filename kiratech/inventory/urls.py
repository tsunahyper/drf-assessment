from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventory.views import InventoryViewSet, InventoryListView, InventoryDetailView

router = DefaultRouter()
router.register(r"inventory", InventoryViewSet, basename="inventory")

urlpatterns = [
    # Template views - these handle /inventory/ routes
    path("", InventoryListView.as_view(), name="inventory-list"),
    path("detail/<int:pk>/", InventoryDetailView.as_view(), name="inventory-detail"),
    # API views - these handle /api/ routes
    path("", include(router.urls)),  # DRF router handles API endpoints
]
