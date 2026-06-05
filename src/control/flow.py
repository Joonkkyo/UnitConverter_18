"""Control flow — FR-FLOW (boundary → control → entity)."""

from boundary.input import parse_input, validate_raw
from boundary.output import format_results
from entity.converter import convert_all
from entity.registry import list_units


def run_conversion(raw_input: str, *, output_format: str = "table") -> str:
    known_units = frozenset(list_units())
    error = validate_raw(raw_input, known_units)
    if error:
        return error
    unit, value = parse_input(raw_input)
    converted = convert_all(unit, value)
    return format_results(unit, value, converted, fmt=output_format)
