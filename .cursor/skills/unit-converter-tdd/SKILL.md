---
name: unit-converter-tdd
description: UnitConverter_18 Dual-Track TDD·ECB 개발 절차
---

# unit-converter-tdd

길이 단위 변환기(meter 기준) **Dual-Track TDD + ECB**. 헌법: `.cursorrules`. Test ID: [reference.md](reference.md).

## 선언 (필수)

`Phase: red|green|refactor` · `Layer: entity|control|boundary` · `Track: Logic|UI` · `Test ID: D-*|U-*`

## Dual-Track

| | Logic | UI |
|---|-------|-----|
| Layer | entity, control | boundary |
| ID | `D-*` | `U-*` |
| Dir | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| Mock | domain **금지** | entity Mock **허용** |

## RED

1. C2C · AAA ([Report/03](../../../Report/03.UnitConverter_RED_TestPlan_Report.md))
2. `tests/` 작성
3. **red Harness:** skeleton + constants/registry 허용 (§5 `.cursorrules`)
4. pytest **FAIL** — `NotImplementedError` / assert / `pytest.fail` OK
5. 보고: 명령줄 · FAIL 유형 · GREEN 함수 1줄

**금지:** converter/input GREEN 선행 · skip/xfail

## GREEN

1. 동일 Test ID 1묶음
2. `src/` **최소** 구현
3. 동일 노드 **PASS**
4. E001~E005 entity 처리 금지 유지

## REFACTOR

- 계약·Test ID 불변 · `tests/entity/` PASS

## pytest

| 시점 | 명령 | 기대 |
|------|------|------|
| Harness | `pytest tests/test_harness_ecb.py -v` | 4 passed |
| RED | `pytest tests/entity/test_d_cvt_01.py -v` | FAIL |
| GREEN | 동일 노드 | PASS |

## 오류 코드

E001~E005 — boundary only. entity raise/catch **금지**.
