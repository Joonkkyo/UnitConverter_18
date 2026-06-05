"""Unit registry — FR-REG."""

from entity.constants import METER_TO_FEET, METER_TO_YARD

_units: dict[str, float] = {
    "meter": 1.0,
    "feet": 1.0 / METER_TO_FEET,
    "yard": 1.0 / METER_TO_YARD,
}


def register_unit(name: str, meters_per_unit: float) -> None:
    if meters_per_unit <= 0:
        raise ValueError("meters_per_unit must be positive")
    if name in _units:
        raise ValueError(f"duplicate unit: {name}")
    _units[name] = meters_per_unit


def get_meters_per_unit(name: str) -> float:
    if name not in _units:
        raise KeyError(name)
    return _units[name]


def list_units() -> list[str]:
    return sorted(_units.keys())
