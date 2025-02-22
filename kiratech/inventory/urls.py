from django.urls import path
from inventory.views import InventoryViewSet

urlpatterns = [
    path('', InventoryViewSet.as_view({'get': 'list'}), name='inventory-list'),
    path('<int:pk>/', InventoryViewSet.as_view({'get': 'retrieve'}), name='inventory-detail'),
]
