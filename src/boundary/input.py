"""Boundary input — FR-IN-* / U-IN track (no entity import)."""

E001 = "E001"
E002 = "E002"
E003 = "E003"
E004 = "E004"
E005 = "E005"


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
        return E004
    if unit not in known_units:
        return E003
    return None


def try_parse_and_validate(
    raw: str,
    known_units: frozenset[str],
) -> tuple[str, float] | str:
    """성공 시 (unit, value), 실패 시 E001~E005."""
    if not raw.strip():
        return E005
    if ":" not in raw:
        return E001
    try:
        unit, value = parse_input(raw)
    except ValueError:
        return E002
    error = validate_parsed(unit, value, known_units)
    return error if error else (unit, value)


def validate_raw(raw: str, known_units: frozenset[str]) -> str | None:
    """parse_input + validate_parsed 편의 함수 (U-IN RED/GREEN)."""
    result = try_parse_and_validate(raw, known_units)
    return result if isinstance(result, str) else None
