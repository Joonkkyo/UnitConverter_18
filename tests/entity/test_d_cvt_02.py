"""D-CVT-02 — FR-CVT-04: yard ↔ meter round-trip."""

import pytest

from entity.constants import FLOAT_TOLERANCE
from entity.converter import from_base, to_base


def test_d_cvt_02_yard_meter_round_trip():
    v = 2.734
    m = to_base("yard", v)
    assert m == pytest.approx(2.5, abs=FLOAT_TOLERANCE)
    back = from_base("yard", 2.5)
    assert back == pytest.approx(2.734025, abs=FLOAT_TOLERANCE)
