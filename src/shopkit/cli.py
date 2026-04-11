from __future__ import annotations

from .checkout import checkout_order
from .models import Address
from .reports import revenue_by_category, top_skus
from .seed import create_sample_inventory



def main() -> None:
    inventory = create_sample_inventory()
    address = Address(country="US", state="CA", postal_code="95014")
    order = checkout_order(
        inventory=inventory,
        requests=[("BK-100", 2), ("BK-200", 1), ("EL-100", 1)],
        address=address,
        coupon_code="save10",
        express=False,
    )

    print("Order summary")
    print("-------------")
    print(f"Items: {order.item_count()}")
    print(f"Subtotal: ${order.subtotal:.2f}")
    print(f"Discount: ${order.discount:.2f}")
    print(f"Shipping: ${order.shipping_cost:.2f}")
    print(f"Tax: ${order.tax:.2f}")
    print(f"Total: ${order.total:.2f}")
    print(f"Revenue by category: {revenue_by_category(order)}")
    print(f"Top SKUs: {top_skus(order)}")


if __name__ == "__main__":
    main()
