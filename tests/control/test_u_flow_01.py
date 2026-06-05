"""U-FLOW-01 — FR-FLOW-01: run_conversion success (table)."""

from control.flow import run_conversion


def test_u_flow_01_meter_table_output():
    result = run_conversion("meter:2.5")
    assert "feet" in result
    assert "yard" in result
    assert "8.2 feet" in result
    assert "2.7 yard" in result
