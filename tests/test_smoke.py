from shopkit.models import Address
from shopkit.checkout import checkout_order
from shopkit.seed import create_sample_inventory


def test_checkout_smoke():
    inventory = create_sample_inventory()
    order = checkout_order(
        inventory,
        [("BK-100", 1), ("FD-100", 2)],
        Address(country="US", state="TX", postal_code="75001"),
        coupon_code=None,
    )
    assert order.total > 0
    assert order.item_count() == 3
