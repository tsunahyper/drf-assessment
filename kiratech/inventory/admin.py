from django.contrib import admin
from .models import Inventory, Supplier

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['inventory_name', 'inventory_supplier', 'inventory_stock', 'inventory_availability']
    search_fields = ['inventory_name']
    list_filter = ['inventory_availability', 'inventory_supplier']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_name']