"""U-IN-05 — FR-IN-05: empty input → E005."""

from boundary.input import validate_raw


def test_u_in_05_empty_returns_e005():
    assert validate_raw("") == "E005"
    assert validate_raw("   ") == "E005"
