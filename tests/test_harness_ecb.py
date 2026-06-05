"""Harness smoke — ECB layers, Dual-Track dirs, import contract."""

import ast
from pathlib import Path

import pytest

from entity.constants import (
    BASE_UNIT,
    DEFAULT_UNITS,
    FLOAT_TOLERANCE,
    METER_TO_FEET,
    METER_TO_YARD,
)
from entity.registry import get_meters_per_unit, list_units

SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
TESTS_ROOT = Path(__file__).resolve().parent


def _py_files(package: str) -> list[Path]:
    return [p for p in (SRC_ROOT / package).glob("*.py") if p.name != "__init__.py"]


def _imports_entity(path: Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("entity"):
            return True
    return False


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
    for name in ("entity", "control", "boundary"):
        assert (TESTS_ROOT / name).is_dir(), f"missing tests/{name}/"


def test_ecb_source_packages_exist():
    for name in ("entity", "control", "boundary"):
        assert (SRC_ROOT / name).is_dir(), f"missing src/{name}/"


def test_entity_does_not_import_upper_layers():
    for path in _py_files("entity"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                assert not node.module.startswith(("boundary", "control")), (
                    f"{path.name} must not import {node.module}"
                )


def test_boundary_does_not_import_entity():
    for path in _py_files("boundary"):
        assert not _imports_entity(path), f"{path.name} must not import entity"


def test_entity_has_no_error_codes():
    for path in _py_files("entity"):
        text = path.read_text(encoding="utf-8")
        assert "E00" not in text, f"{path.name} must not handle E001~E005"


def test_logic_tests_no_domain_mock():
    for track in ("entity",):
        for path in (TESTS_ROOT / track).glob("test_*.py"):
            text = path.read_text(encoding="utf-8")
            assert "patch(" not in text, f"Logic mock forbidden: {path.name}"
            assert "MagicMock" not in text, f"Logic mock forbidden: {path.name}"
