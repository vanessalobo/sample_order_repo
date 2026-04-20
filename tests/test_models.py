import pytest
from shopkit.models import Product, CartItem, Order, Address
from typing import List

def test_cartitem_line_total_basic():
    product = Product(sku="SKU1", name="Test Product", price=10.0, weight_kg=1.0, category="C")
    item = CartItem(product=product, quantity=3)
    assert item.line_total() == 30.00

def test_cartitem_line_total_rounding():
    product = Product(sku="SKU2", name="Test Product", price=10.111, weight_kg=1.0, category="C")
    item = CartItem(product=product, quantity=3)
    assert item.line_total() == 30.33

def test_cartitem_line_total_zero_quantity():
    product = Product(sku="SKU1", name="Test Product", price=10.0, weight_kg=1.0, category="C")
    item = CartItem(product=product, quantity=0)
    assert item.line_total() == 0.0

def test_cartitem_line_weight_basic():
    product = Product(sku="SKU1", name="Test Product", price=10.0, weight_kg=2.5, category="C")
    item = CartItem(product=product, quantity=2)
    assert item.line_weight() == 5.0

def test_cartitem_line_weight_rounding():
    product = Product(sku="SKU2", name="Test Product", price=10.0, weight_kg=0.12345, category="C")
    item = CartItem(product=product, quantity=3)
    assert item.line_weight() == 0.370

def test_cartitem_line_weight_zero_quantity():
    product = Product(sku="SKU1", name="Test Product", price=10.0, weight_kg=2.5, category="C")
    item = CartItem(product=product, quantity=0)
    assert item.line_weight() == 0.0

def test_order_item_count_empty():
    order = Order(items=[])
    assert order.item_count() == 0

def test_order_item_count_single_item():
    product = Product(sku="SKU1", name="Test Product", price=10.0, weight_kg=1.0, category="C")
    item = CartItem(product=product, quantity=5)
    order = Order(items=[item])
    assert order.item_count() == 5

def test_order_item_count_multiple_items():
    product1 = Product(sku="SKU1", name="Test Product 1", price=10.0, weight_kg=1.0, category="C")
    item1 = CartItem(product=product1, quantity=2)
    product2 = Product(sku="SKU2", name="Test Product 2", price=20.0, weight_kg=2.0, category="C")
    item2 = CartItem(product=product2, quantity=3)
    order = Order(items=[item1, item2])
    assert order.item_count() == 5

def test_order_item_count_with_zero_quantity():
    product1 = Product(sku="SKU1", name="Test Product 1", price=10.0, weight_kg=1.0, category="C")
    item1 = CartItem(product=product1, quantity=2)
    product2 = Product(sku="SKU2", name="Test Product 2", price=20.0, weight_kg=2.0, category="C")
    item2 = CartItem(product=product2, quantity=0)
    order = Order(items=[item1, item2])
    assert order.item_count() == 2
