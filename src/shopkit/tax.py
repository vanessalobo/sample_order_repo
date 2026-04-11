from __future__ import annotations

from .models import Address, CartItem
from .utils import round_money


STATE_TAX_RATES = {
    "CA": 0.0725,
    "NY": 0.04,
    "TX": 0.0625,
}


def calculate_tax(items: list[CartItem], address: Address, taxable_subtotal_after_discount: float) -> float:
    if address.country != "US":
        return 0.0

    rate = STATE_TAX_RATES.get(address.state, 0.05)
    taxable_value = 0.0
    taxable_item_total = sum(item.line_total() for item in items if item.product.taxable)
    full_subtotal = sum(item.line_total() for item in items)

    if full_subtotal == 0:
        return 0.0

    taxable_ratio = taxable_item_total / full_subtotal
    taxable_value = taxable_subtotal_after_discount * taxable_ratio
    return round_money(taxable_value * rate)
