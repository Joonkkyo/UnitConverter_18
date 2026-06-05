"""Harness smoke — ECB layers importable, domain SSOT, Dual-Track dirs exist."""

from pathlib import Path

from entity.constants import (
    BASE_UNIT,
    DEFAULT_UNITS,
    FLOAT_TOLERANCE,
    METER_TO_FEET,
    METER_TO_YARD,
)
from entity.registry import get_meters_per_unit, list_units


def test_domain_constants_ssot():
    assert BASE_UNIT == "meter"
    assert METER_TO_FEET == 3.28084
    assert METER_TO_YARD == 1.09361
    assert DEFAULT_UNITS == frozenset({"meter", "feet", "yard"})
    assert FLOAT_TOLERANCE == 1e-4


def test_default_units_registered():
    assert list_units() == ["feet", "meter", "yard"]
    assert get_meters_per_unit("meter") == 1.0


def test_dual_track_directories_exist():
    tests_root = Path(__file__).resolve().parent
    for name in ("entity", "control", "boundary"):
        assert (tests_root / name).is_dir(), f"missing tests/{name}/"


def test_ecb_source_packages_exist():
    src_root = Path(__file__).resolve().parents[1] / "src"
    for name in ("entity", "control", "boundary"):
        assert (src_root / name).is_dir(), f"missing src/{name}/"
