# TODO_RED — RED 단계 선행 · 실행 체크리스트

> **목적:** `/tdd-red`·`/red-skeleton` 전(Ask·설계)과 RED 실행 시 추적.  
> **SSOT 설계:** [Report/03.UnitConverter_RED_TestPlan_Report.md](Report/03.UnitConverter_RED_TestPlan_Report.md)

---

## 0. RED 선행 vs RED 실행

| 구분 | 단계 | 산출 | `src/` |
|------|------|------|--------|
| **선행 (Ask · spec)** | PRD · INTERFACES · Report 03 | 설계표 · C2C · pytest 계획 | **금지** |
| **실행 (red)** | `/red-skeleton` → `/tdd-red` | `tests/` + API skeleton · pytest **FAIL** | skeleton만 ([.cursorrules](.cursorrules) §5) |
| **다음 (green)** | `/green-minimal` | 최소 구현 | 허용 |

---

## 1. 프로젝트 기반 (RED 전체 공통)

| 항목 | 상태 |
|------|------|
| [x] `docs/PRD.md` | spec |
| [x] `docs/INTERFACES.md` | spec |
| [x] Report 01~03 | spec |
| [x] `.cursorrules` | spec |
| [x] `pyproject.toml` + `pip install -e ".[dev]"` | red |
| [x] `src/entity|control|boundary` placeholder | red |
| [x] `tests/conftest.py`, `test_harness_ecb.py` | red |
| [x] `pytest tests/test_harness_ecb.py` → 4 passed | red |
| [x] Command `/tdd-red` (`.cursor/commands/`) | red |
| [x] Skill `unit-converter-tdd/SKILL.md` | red |

---

## 2. RED 묶음 1건당 선행 (Ask)

묶음당 **모두** [x] 후 `/red-skeleton` 또는 `/tdd-red`.

### Logic (Track B)

- [ ] `Phase: red | Layer: entity | Track: Logic | Test ID: …` 선언
- [ ] C2C: PRD · Given/When/Then · `FLOAT_TOLERANCE`
- [ ] RED 설계표: 함수 · Expected Failure
- [ ] pytest 경로 확정
- [ ] spec Ask: `src/` 미수정 · red Harness: skeleton만 · skip/xfail 없음

### UI (Track A)

- [ ] `Phase: red | Layer: boundary | Track: UI | Test ID: …`
- [ ] Then: `"E00x"` · **entity/converter 미호출** (GREEN mock)
- [ ] `tests/boundary/test_u_*.py` 경로

---

## 3. RED 묶음별 진행 상태

| Test ID | PRD | 선행 설계 | RED 실행 | GREEN |
|---------|-----|-----------|----------|-------|
| **D-CVT-01** | FR-CVT-01 | [x] Report 03 | [x] | [x] |
| **D-CVT-02** | FR-CVT-04 | [x] | planned | [ ] |
| **D-CVT-03** | FR-CVT-03 | [x] | [x] | [x] |
| **D-REG-01** | FR-REG-01 | [x] | [ ] | [ ] |
| **U-IN-01** | FR-IN-01 | [x] | [x] | [x] |
| **U-IN-02** | FR-IN-02 | [x] | [x] | [x] |
| **U-IN-03** | FR-IN-03 | [x] | [x] | [x] |
| **U-IN-04** | FR-IN-04 | [x] | [x] | [x] |
| **U-IN-05** | FR-IN-05 | [x] | [x] | [x] |
| **U-OUT-01** | FR-OUT-01 | [x] | [ ] | [ ] |

**권장 RED 순서:** D-CVT-01 → D-CVT-03 → U-IN-01~05 → U-OUT-01 → D-REG-01

---

## 4. RED 실행 체크리스트

- [ ] `tests/` 중심 수정 (red Harness 시 API skeleton·constants/registry 허용 — [.cursorrules](.cursorrules) §5)
- [ ] FAIL 유형: `pytest.fail("RED: …")` · **assert FAIL** · **`NotImplementedError`(stub)** · `ImportError` — exit ≠ 0이면 RED 유효
- [ ] 대상 노드만 `pytest -v`
- [ ] exit ≠ 0 · PASS면 RED 미완료
- [ ] 완료 보고: Phase/Layer/Track/Test ID · 명령줄 · 다음 GREEN 함수 1줄

---

## 5. 완료 정의

**RED 선행(spec) 완료:** Report 03 해당 묶음 설계표 [x] · INTERFACES 매핑 · `src/` 미착수

**RED 실행 완료:** §4 + §3 «RED 실행» [x] + pytest FAIL 증거
