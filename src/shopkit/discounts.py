from __future__ import annotations

from .models import CartItem
from .utils import normalize_coupon, round_money


PERCENTAGE_COUPONS = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
}

FIXED_COUPONS = {
    "WELCOME5": 5.00,
}


def category_discount(items: list[CartItem]) -> float:
    """Books get 5% off when buying 3 or more book items total."""
    book_qty = sum(item.quantity for item in items if item.product.category == "books")
    if book_qty < 3:
        return 0.0
    eligible_subtotal = sum(
        item.line_total() for item in items if item.product.category == "books"
    )
    return round_money(eligible_subtotal * 0.05)



def apply_coupon(subtotal: float, coupon_code: str | None) -> tuple[float, str | None]:
    code = normalize_coupon(coupon_code)
    if code is None:
        return 0.0, None

    if code in PERCENTAGE_COUPONS:
        return round_money(subtotal * PERCENTAGE_COUPONS[code]), code

    if code in FIXED_COUPONS:
        return min(round_money(FIXED_COUPONS[code]), round_money(subtotal)), code

    raise ValueError(f"invalid coupon code: {coupon_code}")
