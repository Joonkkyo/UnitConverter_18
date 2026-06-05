"""U-IN-02 — FR-IN-02: invalid number → E002."""

from boundary.input import validate_raw


def test_u_in_02_invalid_number_returns_e002():
    assert validate_raw("meter:abc") == "E002"
