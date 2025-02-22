from rest_framework.serializers import ModelSerializer, CharField
from .models import Inventory, Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class InventorySerializer(ModelSerializer):
    supplier_name = CharField(source="inventory_supplier.supplier_name", read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"
