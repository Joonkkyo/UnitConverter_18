"""Boundary output — FR-OUT-* (table format)."""

import json


def format_results(
    source_unit: str,
    source_value: float,
    converted: dict[str, float],
    *,
    fmt: str = "table",
) -> str:
    """FR-OUT-01~03."""
    if fmt == "table":
        lines = [
            f"{source_value} {source_unit} = {round(val, 1)} {target}"
            for target, val in sorted(converted.items())
            if target != source_unit
        ]
        return "\n".join(lines)
    if fmt == "json":
        return json.dumps(converted)
    if fmt == "csv":
        header = "unit,value"
        rows = [f"{u},{v}" for u, v in sorted(converted.items())]
        return "\n".join([header, *rows])
    raise ValueError(f"unsupported format: {fmt}")
