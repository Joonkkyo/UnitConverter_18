"""Unit conversion — FR-CVT."""

from entity.registry import get_meters_per_unit, list_units


def to_base(unit: str, value: float) -> float:
    """value [unit] → meter."""
    return value * get_meters_per_unit(unit)


def from_base(unit: str, base_meters: float) -> float:
    """meter → unit."""
    return base_meters / get_meters_per_unit(unit)


def convert_all(source_unit: str, value: float) -> dict[str, float]:
    """Convert value to all registered units."""
    base_meters = to_base(source_unit, value)
    return {unit: from_base(unit, base_meters) for unit in list_units()}
