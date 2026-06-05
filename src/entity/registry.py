"""Unit registry — FR-REG."""

from entity.constants import BASE_UNIT, DEFAULT_UNITS, METER_TO_FEET, METER_TO_YARD


def _default_meters_per_unit(name: str) -> float:
    if name == BASE_UNIT:
        return 1.0
    if name == "feet":
        return 1.0 / METER_TO_FEET
    if name == "yard":
        return 1.0 / METER_TO_YARD
    raise ValueError(f"unsupported default unit: {name}")


_units: dict[str, float] = {
    name: _default_meters_per_unit(name) for name in DEFAULT_UNITS
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
