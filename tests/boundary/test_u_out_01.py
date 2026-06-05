"""U-OUT-01 — FR-OUT-01: table format with 1-decimal rounding."""

from boundary.output import format_results


def test_u_out_01_table_one_decimal():
    converted = {"meter": 2.5, "feet": 8.2021, "yard": 2.734025}
    result = format_results("meter", 2.5, converted, fmt="table")
    assert "2.5 meter = 8.2 feet" in result
    assert "2.5 meter = 2.7 yard" in result
    assert "2.5 meter = 2.5 meter" not in result
