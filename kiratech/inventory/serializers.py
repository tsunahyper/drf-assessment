from rest_framework import serializers
from .models import Inventory, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_id', 'supplier_name']

class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='inventory_supplier.supplier_name', read_only=True)

    class Meta:
        model = Inventory
        fields = ['inventory_id', 'inventory_name', 'inventory_description', 
                 'inventory_note', 'inventory_stock', 'inventory_availability', 
                 'inventory_supplier', 'supplier_name']