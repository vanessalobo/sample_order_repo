from __future__ import annotations

from collections import defaultdict

from .models import Order
from .utils import round_money


def average_item_price(order: Order) -> float:
    total_quantity = 0
    total_value = 0.0

    for item in order.items:
        total_quantity += item.quantity
        total_value += item.line_total()

    if total_quantity == 0:
        return 0.0

    return round_money(total_value / total_quantity)


def category_quantity_breakdown(order: Order) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)

    for item in order.items:
        counts[item.product.category] += item.quantity

    return dict(sorted(counts.items()))


def most_expensive_item(order: Order) -> tuple[str, float] | None:
    if not order.items:
        return None

    max_item = max(order.items, key=lambda item: (item.product.price, item.product.sku))
    return (max_item.product.sku, round_money(max_item.product.price))


def has_bulk_discount_eligible_items(order: Order, min_quantity: int = 10) -> bool:
    for item in order.items:
        if item.quantity >= min_quantity:
            return True
    return False


def category_share(order: Order) -> dict[str, float]:
    revenue_by_category: dict[str, float] = defaultdict(float)
    total_revenue = 0.0

    for item in order.items:
        line_total = item.line_total()
        revenue_by_category[item.product.category] += line_total
        total_revenue += line_total

    if total_revenue == 0:
        return {}

    shares = {
        category: round_money((revenue / total_revenue) * 100.0)
        for category, revenue in sorted(revenue_by_category.items())
    }

    return shares