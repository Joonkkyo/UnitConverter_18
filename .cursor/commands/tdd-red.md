# TDD RED — 실패 테스트 먼저

UnitConverter_18 **Dual-Track TDD** — **RED 단계**. pytest **FAIL** 확인.

## 필수 선언

```text
Phase: red | Layer: entity|control|boundary | Track: Logic|UI | Test ID: D-* 또는 U-*
```

예: `Phase: red | Layer: entity | Track: Logic | Test ID: D-CVT-01`

- **Logic:** `tests/entity/test_d_*.py`, `tests/control/`
- **UI:** `tests/boundary/test_u_*.py`
- 헌법: `.cursorrules` · Skill: `unit-converter-tdd` · ID: `reference.md`

## red 브랜치 Harness (`src/`)

`.cursorrules` §5 — **API skeleton 허용:**

- ✅ `entity.constants` (SSOT), `entity.registry` (기본 3단위·조회)
- ✅ `NotImplementedError` stub (`converter`, `boundary`, `control`)
- ❌ 비즈니스 로직 구현 (GREEN까지)

## 절차

1. Test ID · PRD/C2C · pytest 경로 확정
2. AAA — Given / When / Then (`FLOAT_TOLERANCE`, E001~E005)
3. `tests/` 작성 (red Harness 시 skeleton 병행 가능)
4. `python -m pytest <file>::<node> -v` → **FAIL**
5. 보고: FAIL 유형 · 명령줄 · GREEN 시 구현 함수 1줄

## FAIL 유형 (RED 유효)

| 유형 | 조건 |
|------|------|
| `NotImplementedError` | stub 호출 (red 기본) |
| assert FAIL | Then 불일치 |
| `pytest.fail("RED: …")` | 스켈레톤 only |
| `ImportError` | Harness 미완 시만 |

**PASS면 RED 미완료**

## pytest 예시

```bash
python -m pytest tests/entity/test_d_cvt_01.py -v
python -m pytest tests/boundary/test_u_in_01.py -v
python -m pytest tests/test_harness_ecb.py -v   # 4 passed (smoke)
```

## 금지

- GREEN 로직 선행 (`converter`, `validate_raw` 등)
- Logic Track Domain Mock
- skip / xfail / assert 완화
