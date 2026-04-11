from __future__ import annotations

from dataclasses import dataclass

from .models import Product


@dataclass
class StockRecord:
    product: Product
    quantity: int


class InventoryManager:
    def __init__(self) -> None:
        self._stock: dict[str, StockRecord] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        if product.sku in self._stock:
            self._stock[product.sku].quantity += quantity
        else:
            self._stock[product.sku] = StockRecord(product=product, quantity=quantity)

    def has_sku(self, sku: str) -> bool:
        return sku in self._stock

    def get_product(self, sku: str) -> Product:
        if sku not in self._stock:
            raise KeyError(f"unknown sku: {sku}")
        return self._stock[sku].product

    def available_quantity(self, sku: str) -> int:
        if sku not in self._stock:
            return 0
        return self._stock[sku].quantity

    def reserve(self, sku: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        record = self._stock.get(sku)
        if record is None:
            raise KeyError(f"unknown sku: {sku}")
        if record.quantity < quantity:
            raise ValueError(
                f"insufficient stock for {sku}: requested {quantity}, available {record.quantity}"
            )
        record.quantity -= quantity

    def restock(self, sku: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if sku not in self._stock:
            raise KeyError(f"unknown sku: {sku}")
        self._stock[sku].quantity += quantity

    def list_skus(self) -> list[str]:
        return sorted(self._stock.keys())
