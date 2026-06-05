"""D-CVT-03 — FR-CVT-03: convert_all from meter."""

import pytest

from entity.constants import FLOAT_TOLERANCE
from entity.converter import convert_all


def test_d_cvt_03_meter_convert_all_default_units(default_registry):
    # Given: default registry (meter, feet, yard)
    assert set(default_registry) == {"meter", "feet", "yard"}
    # When: meter:2.5
    result = convert_all("meter", 2.5)
    # Then: all default units
    assert set(result.keys()) == {"meter", "feet", "yard"}
    assert result["meter"] == pytest.approx(2.5, abs=FLOAT_TOLERANCE)
    assert result["feet"] == pytest.approx(8.2021, abs=FLOAT_TOLERANCE)
    assert result["yard"] == pytest.approx(2.734025, abs=FLOAT_TOLERANCE)
