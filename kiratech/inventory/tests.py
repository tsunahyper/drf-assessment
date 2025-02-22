from django.test import TestCase, Client
from django.urls import reverse
from .models import Inventory, Supplier
from django.contrib.auth.models import User


class InventoryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.supplier = Supplier.objects.create(supplier_name="Test Supplier")
        self.inventory = Inventory.objects.create(
            inventory_name="Test Item",
            inventory_description="Test Description",
            inventory_note="Test Note",
            inventory_stock=10,
            inventory_availability=True,
            inventory_supplier=self.supplier,
        )

    def test_inventory_list_view(self):
        response = self.client.get(reverse("inventory-list"))
        self.assertEqual(response.status_code, 200)
        print("The “/inventory”page returns 200 OK status")

    def test_inventory_detail_view(self):
        response = self.client.get(
            reverse("inventory-detail", args=[self.inventory.inventory_id])
        )
        self.assertEqual(response.status_code, 200)
        print("The “/inventory/<id>/”page returns 200 OK status")

    def test_inventory_api(self):
        response = self.client.get("/api/inventory/")
        self.assertEqual(response.status_code, 200)
        print("The “/api/inventory”page returns 200 OK status")
