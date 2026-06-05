"""Shared pytest fixtures."""

import pytest

from entity.constants import DEFAULT_UNITS
from entity.registry import list_units


@pytest.fixture
def default_registry():
    """Module-level registry — meter/feet/yard 기본 등록 (GREEN 시 register_unit 확장)."""
    units = list_units()
    assert set(units) == set(DEFAULT_UNITS)
    return units
