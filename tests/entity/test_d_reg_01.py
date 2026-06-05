"""D-REG-01 — FR-REG-01: register_unit (cubit)."""

import pytest

import entity.registry as registry
from entity.converter import convert_all
from entity.registry import get_meters_per_unit, register_unit


def test_d_reg_01_register_cubit_convert():
    snapshot = dict(registry._units)
    try:
        register_unit("cubit", 0.4572)
        assert get_meters_per_unit("cubit") == pytest.approx(0.4572)
        result = convert_all("cubit", 1)
        assert result["meter"] == pytest.approx(0.4572, abs=1e-4)
    finally:
        registry._units.clear()
        registry._units.update(snapshot)
