# shopkit

A small sample Python repository for AI code analysis and automated test generation.

## Features
- Inventory management
- Cart operations
- Discounts and coupon handling
- Shipping calculation
- Order checkout
- Sales reporting

## Structure
- `src/shopkit/models.py` - dataclasses for products, carts, orders
- `src/shopkit/inventory.py` - in-memory inventory manager
- `src/shopkit/discounts.py` - coupon and discount logic
- `src/shopkit/shipping.py` - shipping rules
- `src/shopkit/checkout.py` - end-to-end order checkout flow
- `src/shopkit/reports.py` - simple reporting helpers
- `src/shopkit/utils.py` - utility helpers
- `src/shopkit/seed.py` - sample data
- `src/shopkit/cli.py` - runnable example

## Run
```bash
python -m shopkit.cli
```

## Notes
This repo is intentionally small but non-trivial:
- logic spans multiple files
- there are validation branches and error paths
- numeric behavior is deterministic enough for test generation
