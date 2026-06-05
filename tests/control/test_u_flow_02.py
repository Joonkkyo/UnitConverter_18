"""U-FLOW-02 — validation error skips convert_all (UI mock allowed)."""

from unittest.mock import patch

from control.flow import run_conversion


def test_u_flow_02_negative_skips_convert_all():
    with patch("control.flow.convert_all") as mock_convert:
        assert run_conversion("meter:-1") == "E004"
        mock_convert.assert_not_called()


def test_u_flow_02_unknown_unit_skips_convert_all():
    with patch("control.flow.convert_all") as mock_convert:
        assert run_conversion("mile:1") == "E003"
        mock_convert.assert_not_called()
