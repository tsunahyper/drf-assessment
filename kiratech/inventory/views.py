from .models import Inventory
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import InventorySerializer

class InventoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'note', 'supplier__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.query_params.get('supplier_id')
        if supplier_id:
            queryset = queryset.filter(supplier_id=supplier_id)
        return queryset
        