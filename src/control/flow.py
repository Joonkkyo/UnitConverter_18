"""Control flow — FR-FLOW (boundary → control → entity)."""

from boundary.input import try_parse_and_validate
from boundary.output import format_results
from entity.converter import convert_all
from entity.registry import list_units


def run_conversion(raw_input: str, *, output_format: str = "table") -> str:
    known_units = frozenset(list_units())
    parsed = try_parse_and_validate(raw_input, known_units)
    if isinstance(parsed, str):
        return parsed
    unit, value = parsed
    converted = convert_all(unit, value)
    return format_results(unit, value, converted, fmt=output_format)
