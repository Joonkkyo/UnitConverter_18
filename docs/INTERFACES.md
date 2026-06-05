# INTERFACES — UnitConverter_XX (테스트·구현 SSOT)

> 작성일: 2026-06-05  
> 연계: [PRD.md](PRD.md) · [Report/02.UnitConverter_Interface_Architecture_Report.md](../Report/02.UnitConverter_Interface_Architecture_Report.md)  
> 목적: **RED/GREEN 단계에서 mock·구현의 계약**을 고정한다. spec 브랜치에서는 **시그니처·불변식만** 정의하고 `src/` 구현은 RED 이후.

---

## 1. 레이어·의존 방향

```
boundary (input, output, config_loader)
    ↓
control (flow)
    ↓
entity (constants, registry, converter)
```

- **금지:** `entity` 가 `control` / `boundary` import
- **금지 (Logic Track):** entity 함수를 `unittest.mock` 으로 대체

---

## 2. Entity — `src/entity/`

### 2.1 `constants.py` (SSOT)

```python
BASE_UNIT: str = "meter"
METER_TO_FEET: float = 3.28084
METER_TO_YARD: float = 1.09361
DEFAULT_UNITS: frozenset[str]  # {"meter", "feet", "yard"}
FLOAT_TOLERANCE: float = 1e-4   # pytest approx
```

| 불변식 | 설명 |
|--------|------|
| I-CST-01 | 비율 리터럴은 **이 파일만** (다른 모듈 `3.28084` 산재 금지) |
| I-CST-02 | `BASE_UNIT == "meter"` |

---

### 2.2 `registry.py`

```python
def register_unit(name: str, meters_per_unit: float) -> None:
    """
    1 name = meters_per_unit meter.
    name 중복 시 ValueError (테스트: D-REG-02).
    meters_per_unit <= 0 → ValueError.
    """

def get_meters_per_unit(name: str) -> float:
    """미등록 name → KeyError (entity; boundary는 E003으로 매핑)."""

def list_units() -> list[str]:
    """등록 순서 또는 정렬 규약: 알파벳 오름차순 (테스트 고정)."""
```

| 불변식 | 설명 |
|--------|------|
| I-REG-01 | 초기화 시 `meter`, `feet`, `yard` 기본 등록 |
| I-REG-02 | `register_unit` 후 `list_units()` 에 포함 |

**기본 등록값 (meter 기준)**

| unit | meters_per_unit | 의미 |
|------|-----------------|------|
| meter | 1.0 | 1 m = 1 m |
| feet | 1/3.28084 | 1 ft = (1/3.28084) m |
| yard | 1/1.09361 | 1 yd = (1/1.09361) m |

---

### 2.3 `converter.py`

```python
def to_base(unit: str, value: float) -> float:
    """value [unit] → meter."""

def from_base(unit: str, base_meters: float) -> float:
    """meter → unit."""

def convert_all(source_unit: str, value: float) -> dict[str, float]:
    """
    등록된 모든 단위에 대한 값.
    키: 단위명, 값: 환산 결과 (float).
    source_unit 항목 포함, 동일 입력이면 value와 일치(오차 내).
    """
```

| 불변식 | 설명 |
|--------|------|
| I-CVT-01 | `to_base(u, v)` 후 `from_base(u, m)` ≈ `v` (round-trip) |
| I-CVT-02 | `convert_all` 키 집합 == `list_units()` |
| I-CVT-03 | feet↔yard 는 meter 경유와 동일 결과 |

---

## 3. Control — `src/control/`

### 3.1 `flow.py`

```python
def run_conversion(
    raw_input: str,
    *,
    output_format: str = "table",
) -> str:
    """
    1. boundary.input.parse_input
    2. boundary.input.validate → 에러 시 에러 코드 문자열 반환 또는 예외 (프로젝트 규약: str 반환 권장 U-OUT와 통일)
    3. entity.converter.convert_all
    4. boundary.output.format_results
    """
```

| 불변식 | 설명 |
|--------|------|
| I-FLOW-01 | 검증 실패 시 **entity.converter 호출 없음** (UI Track GREEN에서 mock 검증) |
| I-FLOW-02 | 성공 시 반환 문자열 비어 있지 않음 |

---

## 4. Boundary — `src/boundary/`

### 4.1 `input.py`

```python
def parse_input(raw: str) -> tuple[str, float]:
    """
    FR-IN-06. 'unit:value' — split(':', 1).
    실패: ValueError + 메시지 (내부); validate 단계에서 E00x 매핑.
    """

def validate_parsed(unit: str, value: float, known_units: frozenset[str]) -> str | None:
    """
    None = OK.
    else E003/E004. known_units는 control이 list_units()로 주입 (boundary→entity 직접 import 금지).
    """

def validate_raw(raw: str, known_units: frozenset[str]) -> str | None:
    """
    parse_input + validate_parsed 편의 함수 (U-IN RED/GREEN).
    None = OK, else "E001".."E005".
    """
```

**에러 코드 (boundary SSOT)**

| 코드 | FR | 조건 |
|------|-----|------|
| E001 | FR-IN-01 | `:` 없음 |
| E002 | FR-IN-02 | 숫자 파싱 실패 |
| E003 | FR-IN-03 | 미등록 단위 |
| E004 | FR-IN-04 | 음수 |
| E005 | FR-IN-05 | 빈 입력 |

| 불변식 | 설명 |
|--------|------|
| I-IN-01 | entity **import 금지** — registry 조회는 `validate` 에서 이름만 비교하거나 registry 인터페이스 주입 (GREEN 설계 선택) |
| I-IN-02 | E001~E005 는 **entity에서 raise 금지** |

---

### 4.2 `output.py`

```python
def format_results(
    source_unit: str,
    source_value: float,
    converted: dict[str, float],
    *,
    fmt: Literal["table", "json", "csv"] = "table",
) -> str:
    """FR-OUT-01~03."""
```

**표 형식 (FR-OUT-01) — README 예시**

```
{source_value} {source_unit} = {x} {target_unit}
```

표시 소수: **소수점 1자리 반올림** (README `8.2`, `2.7` 와 호환 — U-OUT-01에서 고정)

---

### 4.3 `config_loader.py` (P2)

```python
def load_units_from_file(path: str | Path) -> None:
    """JSON/YAML → register_unit 반복. FR-CFG-01."""
```

---

## 5. Protocol 요약 (테스트 더블·GREEN 최소 구현용)

```python
from typing import Protocol

class UnitRegistry(Protocol):
    def register_unit(self, name: str, meters_per_unit: float) -> None: ...
    def get_meters_per_unit(self, name: str) -> float: ...
    def list_units(self) -> list[str]: ...

class UnitConverterPort(Protocol):
    def to_base(self, unit: str, value: float) -> float: ...
    def from_base(self, unit: str, base_meters: float) -> float: ...
    def convert_all(self, source_unit: str, value: float) -> dict[str, float]: ...
```

OCP: 새 단위는 **registry 등록만** — `UnitConverterPort` 구현체의 분기 추가 없이 동작.

---

## 6. 테스트 ID ↔ 인터페이스 매핑

| Test ID | 주 인터페이스 | pytest 경로 (예정) |
|---------|--------------|-------------------|
| D-CVT-01 | `to_base`, `from_base` | `tests/entity/test_d_cvt_01.py` |
| D-CVT-03 | `convert_all` | `tests/entity/test_d_cvt_03.py` |
| D-REG-01 | `register_unit` | `tests/entity/test_d_reg_01.py` |
| D-CFG-01 | `load_units_from_file` | `tests/entity/test_d_cfg_01.py` |
| U-IN-01~05 | `parse_input`, `validate_parsed` | `tests/boundary/test_u_in_*.py` |
| U-OUT-01~03 | `format_results` | `tests/boundary/test_u_out_*.py` |
| U-FLOW-01 | `run_conversion` | `tests/control/test_u_flow_01.py` |

전체 목록: [.cursor/skills/unit-converter-tdd/reference.md](../.cursor/skills/unit-converter-tdd/reference.md)

---

## 7. 프로토타입 매핑 (`UnitConverter.py` → 목표)

| 프로토타입 줄 | 목표 인터페이스 |
|--------------|----------------|
| `':' not in input_str` | `parse_input` / E001 |
| `float(value_str)` | `parse_input` / E002 |
| `if unit == "meter"` … | `registry` + `to_base` |
| `meter_value * 3.28084` | `from_base("feet", …)` |
| `print(f"...")` | `format_results(..., "table")` |
