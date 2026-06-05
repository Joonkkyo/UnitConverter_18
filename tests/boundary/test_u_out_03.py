"""U-OUT-03 — FR-OUT-03: CSV output."""

from boundary.output import format_results


def test_u_out_03_csv_header_and_rows():
    converted = {"feet": 8.2021, "meter": 2.5, "yard": 2.734025}
    result = format_results("meter", 2.5, converted, fmt="csv")
    lines = result.splitlines()
    assert lines[0] == "unit,value"
    assert "feet,8.2021" in lines
    assert "yard,2.734025" in lines
