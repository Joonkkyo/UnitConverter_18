"""Boundary input — FR-IN-* / U-IN track (no entity import)."""


def parse_input(raw: str) -> tuple[str, float]:
    """FR-IN-06. 'unit:value' — raises ValueError on parse failure."""
    stripped = raw.strip()
    if ":" not in stripped:
        raise ValueError("invalid format")
    unit, value_str = stripped.split(":", 1)
    try:
        value = float(value_str)
    except ValueError as exc:
        raise ValueError("invalid number") from exc
    return unit, value


def validate_parsed(
    unit: str,
    value: float,
    known_units: frozenset[str],
) -> str | None:
    """None = OK, else E003/E004 (format errors handled in validate_raw)."""
    if value < 0:
        return "E004"
    if unit not in known_units:
        return "E003"
    return None


def validate_raw(raw: str, known_units: frozenset[str]) -> str | None:
    """Parse + validate; None = OK, else E001..E005."""
    if not raw.strip():
        return "E005"
    if ":" not in raw:
        return "E001"
    unit, value_str = raw.split(":", 1)
    try:
        value = float(value_str)
    except ValueError:
        return "E002"
    return validate_parsed(unit, value, known_units)
