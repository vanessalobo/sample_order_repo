from __future__ import annotations

from .models import Address, CartItem
from .utils import round_money


DOMESTIC_STATES_NO_RURAL_SURCHARGE = {"CA", "NY", "TX", "WA"}


def calculate_shipping(items: list[CartItem], address: Address, express: bool = False) -> float:
    total_weight = sum(item.line_weight() for item in items)
    if total_weight == 0:
        return 0.0

    if address.country != "US":
        base = 18.0 + 7.5 * total_weight
    else:
        base = 4.0 + 1.25 * total_weight
        if address.state not in DOMESTIC_STATES_NO_RURAL_SURCHARGE:
            base += 2.5

    if express:
        base *= 1.8

    if total_weight > 20:
        base += 10.0

    return round_money(base)
