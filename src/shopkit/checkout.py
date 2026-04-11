from __future__ import annotations

from .discounts import apply_coupon, category_discount
from .inventory import InventoryManager
from .models import Address, CartItem, Order
from .shipping import calculate_shipping
from .tax import calculate_tax
from .utils import round_money



def checkout_order(
    inventory: InventoryManager,
    requests: list[tuple[str, int]],
    address: Address,
    coupon_code: str | None = None,
    express: bool = False,
) -> Order:
    if not requests:
        raise ValueError("cannot checkout an empty cart")

    items: list[CartItem] = []
    for sku, quantity in requests:
        if quantity <= 0:
            raise ValueError(f"quantity for {sku} must be positive")
        product = inventory.get_product(sku)
        items.append(CartItem(product=product, quantity=quantity))

    for item in items:
        inventory.reserve(item.product.sku, item.quantity)

    subtotal = round_money(sum(item.line_total() for item in items))
    auto_discount = category_discount(items)
    coupon_discount, normalized_coupon = apply_coupon(subtotal - auto_discount, coupon_code)
    total_discount = round_money(auto_discount + coupon_discount)
    discounted_subtotal = round_money(max(subtotal - total_discount, 0.0))
    shipping_cost = calculate_shipping(items, address, express=express)
    tax = calculate_tax(items, address, discounted_subtotal)
    total = round_money(discounted_subtotal + shipping_cost + tax)

    return Order(
        items=items,
        subtotal=subtotal,
        discount=total_discount,
        shipping_cost=shipping_cost,
        tax=tax,
        total=total,
        applied_coupon=normalized_coupon,
    )
