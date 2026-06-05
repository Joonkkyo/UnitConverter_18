"""U-OUT-02 — FR-OUT-02: JSON output."""

import json

from boundary.output import format_results


def test_u_out_02_json_keys_and_values():
    converted = {"meter": 2.5, "feet": 8.2021, "yard": 2.734025}
    result = format_results("meter", 2.5, converted, fmt="json")
    assert json.loads(result) == converted
