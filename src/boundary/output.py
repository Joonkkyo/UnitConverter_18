"""Boundary output — FR-OUT-* (table format)."""

import json

TABLE_DECIMAL_PLACES = 1


def _format_table(
    source_unit: str,
    source_value: float,
    converted: dict[str, float],
) -> str:
    lines = [
        f"{source_value} {source_unit} = {round(val, TABLE_DECIMAL_PLACES)} {target}"
        for target, val in sorted(converted.items())
        if target != source_unit
    ]
    return "\n".join(lines)


def _format_json(converted: dict[str, float]) -> str:
    return json.dumps(converted)


def _format_csv(converted: dict[str, float]) -> str:
    header = "unit,value"
    rows = [f"{u},{v}" for u, v in sorted(converted.items())]
    return "\n".join([header, *rows])


def format_results(
    source_unit: str,
    source_value: float,
    converted: dict[str, float],
    *,
    fmt: str = "table",
) -> str:
    """FR-OUT-01~03."""
    match fmt:
        case "table":
            return _format_table(source_unit, source_value, converted)
        case "json":
            return _format_json(converted)
        case "csv":
            return _format_csv(converted)
        case _:
            raise ValueError(f"unsupported format: {fmt}")
