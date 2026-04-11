from __future__ import annotations

from collections import defaultdict

from .models import Order
from .utils import round_money



def revenue_by_category(order: Order) -> dict[str, float]:
    revenue: dict[str, float] = defaultdict(float)
    for item in order.items:
        revenue[item.product.category] += item.line_total()
    return {key: round_money(value) for key, value in sorted(revenue.items())}



def top_skus(order: Order, limit: int = 3) -> list[tuple[str, int]]:
    counts: dict[str, int] = defaultdict(int)
    for item in order.items:
        counts[item.product.sku] += item.quantity
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:limit]
