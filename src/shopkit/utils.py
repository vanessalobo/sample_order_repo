from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low cannot be greater than high")
    return max(low, min(high, value))


def normalize_coupon(code: str | None) -> str | None:
    if code is None:
        return None
    cleaned = code.strip().upper()
    return cleaned or None


def round_money(value: float) -> float:
    return round(value + 1e-9, 2)
