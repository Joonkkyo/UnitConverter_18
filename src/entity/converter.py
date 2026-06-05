"""Unit conversion — FR-CVT (skeleton)."""


def to_base(unit: str, value: float) -> float:
    raise NotImplementedError("GREEN: entity.converter.to_base")


def from_base(unit: str, base_meters: float) -> float:
    raise NotImplementedError("GREEN: entity.converter.from_base")


def convert_all(source_unit: str, value: float) -> dict[str, float]:
    raise NotImplementedError("GREEN: entity.converter.convert_all")
