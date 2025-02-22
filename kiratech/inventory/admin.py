from django.contrib import admin
from inventory.models import Inventory, Supplier

admin.site.register([Inventory, Supplier])
