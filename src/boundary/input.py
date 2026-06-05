"""Boundary input — FR-IN-* / U-IN track (skeleton)."""


def parse_input(raw: str) -> tuple[str, float]:
    raise NotImplementedError("GREEN: boundary.input.parse_input")


def validate_parsed(unit: str, value: float) -> str | None:
    raise NotImplementedError("GREEN: boundary.input.validate_parsed")


def validate_raw(raw: str) -> str | None:
    """Parse + validate; None = OK, else E001..E005."""
    raise NotImplementedError("GREEN: boundary.input.validate_raw")
