"""U-IN-03 — FR-IN-03: unknown unit → E003."""

from boundary.input import validate_raw


def test_u_in_03_unknown_unit_returns_e003():
    assert validate_raw("mile:1") == "E003"
