from django.db.models import (
    Model,
    CASCADE,
    CharField,
    TextField,
    ForeignKey,
    BigAutoField,
    IntegerField,
    BooleanField,
)


class Supplier(Model):
    supplier_id = BigAutoField(primary_key=True, unique=True, editable=False)
    supplier_name = CharField(max_length=200)

    def __str__(self):
        return self.supplier_name


class Inventory(Model):
    inventory_id = BigAutoField(primary_key=True, unique=True, editable=False)
    inventory_name = CharField(max_length=200)
    inventory_description = CharField(max_length=500)
    inventory_note = TextField()
    inventory_stock = IntegerField(default=0)
    inventory_availability = BooleanField(default=True)
    inventory_supplier = ForeignKey(Supplier, on_delete=CASCADE)

    def __str__(self):
        return self.inventory_name
