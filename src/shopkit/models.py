from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float
    weight_kg: float
    category: str
    taxable: bool = True


@dataclass
class CartItem:
    product: Product
    quantity: int

    def line_total(self) -> float:
        return round(self.product.price * self.quantity, 2)

    def line_weight(self) -> float:
        return round(self.product.weight_kg * self.quantity, 3)


@dataclass
class Address:
    country: str
    state: str
    postal_code: str


@dataclass
class Order:
    items: List[CartItem] = field(default_factory=list)
    subtotal: float = 0.0
    discount: float = 0.0
    shipping_cost: float = 0.0
    tax: float = 0.0
    total: float = 0.0
    applied_coupon: str | None = None

    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)
