"""U-IN-01 — FR-IN-01: no colon → E001."""

from boundary.input import validate_raw


def test_u_in_01_no_colon_returns_e001():
    assert validate_raw("meter2.5") == "E001"
