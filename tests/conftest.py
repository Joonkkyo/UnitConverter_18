"""Shared pytest fixtures."""

import pytest

from entity.constants import FLOAT_TOLERANCE


@pytest.fixture
def approx_tol():
    return FLOAT_TOLERANCE
