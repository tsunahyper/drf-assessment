from django.contrib import admin
from .models import Inventory, Supplier

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'stock', 'availability']
    search_fields = ['name']
    list_filter = ['availability', 'supplier']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']