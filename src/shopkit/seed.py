from __future__ import annotations

from .inventory import InventoryManager
from .models import Product



def create_sample_inventory() -> InventoryManager:
    inventory = InventoryManager()
    products = [
        Product(sku="BK-100", name="Clean Code", price=30.00, weight_kg=0.4, category="books", taxable=True),
        Product(sku="BK-200", name="Design Patterns", price=45.00, weight_kg=0.6, category="books", taxable=True),
        Product(sku="EL-100", name="Wireless Mouse", price=25.50, weight_kg=0.2, category="electronics", taxable=True),
        Product(sku="FD-100", name="Coffee Beans", price=18.75, weight_kg=1.0, category="grocery", taxable=False),
        Product(sku="HM-100", name="Desk Lamp", price=22.00, weight_kg=1.5, category="home", taxable=True),
    ]
    for product in products:
        inventory.add_product(product, quantity=20)
    return inventory
