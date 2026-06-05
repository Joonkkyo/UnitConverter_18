"""U-IN-04 — FR-IN-04: negative value → E004."""

from boundary.input import validate_parsed


def test_u_in_04_negative_returns_e004():
    assert validate_parsed("meter", -1.0) == "E004"
