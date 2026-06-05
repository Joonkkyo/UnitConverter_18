"""D-CVT-01 — FR-CVT-01/02: feet ↔ meter round-trip."""

import pytest

from entity.constants import FLOAT_TOLERANCE
from entity.converter import from_base, to_base


def test_d_cvt_01_feet_meter_round_trip():
    # Given: v = 8.2021 (≈ 2.5 m × 3.28084)
    v = 8.2021
    # When / Then: to_base → meter, from_base → feet
    m = to_base("feet", v)
    assert m == pytest.approx(2.5, abs=FLOAT_TOLERANCE)
    back = from_base("feet", 2.5)
    assert back == pytest.approx(8.2021, abs=FLOAT_TOLERANCE)
