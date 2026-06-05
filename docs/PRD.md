# PRD — UnitConverter_XX (길이 단위 변환기)

> 작성일: 2026-06-05  
> SSOT: Mom Test · [Report/01.UnitConverter_ProblemDefinition_Report.md](../Report/01.UnitConverter_ProblemDefinition_Report.md)  
> 선행 코드: `UnitConverter.py` (프로토타입 · 리팩터 대상)

## 1. 배경 (Mom Test)

### 페르소나

길이 단위(**meter · feet · yard**)를 수업·실무에서 자주 바꿔 쓰는 **학습자·실습자**.  
`단위:값` 한 줄 입력으로 **같은 길이의 다른 단위 표현**을 한꺼번에 보고 싶다.

### 진짜 문제 (한 문장)

**여러 단위로 같은 길이를 맞출 때 환산 비율을 손으로 계산하거나 코드에 비율을 박아 넣다가 오류·누락이 나고, 단위를 추가할 때마다 `if/elif` 분기를 늘려야 해서 변경 범위가 커진다.**

### Mom Test 증거

1. `meter:2.5`처럼 입력했을 때 **feet·yard 등 나머지 단위를 바로** 보고 싶다.
2. `1 meter = 3.28084 feet` 같은 **비율을 매번 외우거나 재계산**하기 부담스럽다.
3. 새 단위(예: cubit)를 쓰려면 **기존 변환 코드를 직접 수정**해야 한다고 느낀다.

### 표면 문제 (비목표로 격리)

「Python **단위 변환 프로그램**을 만든다」— 솔루션(TDD, JSON 출력, Cursor)이 문제 정의에 섞인 문장.

본 PRD 1차 목표는 **기준 단위(meter) 기반으로 정확히 환산**하고, **입력 검증·확장(OCP)** 을 테스트로 증명할 수 있는 구조를 만드는 것이다.

---

## 2. 목표

| 우선순위 | 목표 |
|----------|------|
| P0 | `단위:값` 입력 → 지원 단위 **전부**로 변환 결과 제공 (기본 3단위) |
| P0 | 환산 비율 SSOT 준수 (`meter` 기준) · **pytest로 정확도 검증** |
| P0 | 잘못된 형식·숫자·미지원 단위·음수 **거부** (에러 코드) |
| P1 | OCP — 새 단위 추가 시 **기존 변환 로직 분기 최소화** |
| P1 | SRP — 파싱·검증·환산·출력 **책임 분리** (ECB) |
| P2 | 설정 파일(JSON/YAML)에서 비율 로드 |
| P2 | 런타임 단위 등록 (`1 cubit = 0.4572 meter`) |
| P2 | 출력 포맷 선택 (표 / JSON / CSV) |

---

## 3. 비목표

- GUI·웹 프론트엔드 · 배포 파이프라인
- 질량·온도 등 **길이 외** 물리량 (1차)
- 국제단위 전체 카탈로그 · 실시간 환율 API
- 세션(spec)에서 **Domain GREEN 전부 완료** (워크플로·RED 설계 우선)
- “대충 8.2”만 수동 확인 — **pytest 수치 검증** 없이 완료 처리

---

## 4. 사용자

| 구분 | 설명 |
|------|------|
| **Primary** | meter/feet/yard 변환이 필요한 **학습자** (README 실습) |
| **Secondary** | TDD · OCP/SRP · Cursor red/green/refactor **실습자** |

---

## 5. 도메인 규칙

| 규칙 | 설명 |
|------|------|
| R-01 | **기준 단위(base)** 는 `meter` |
| R-02 | `1 meter = 3.28084 feet` (고정 비율, 설정 외부화 시에도 동일 의미) |
| R-03 | `1 meter = 1.09361 yard` |
| R-04 | feet ↔ yard 는 **meter 경유** (직접 상수 하드코딩 지양) |
| R-05 | 입력 형식: `unit:value` — 콜론 1개, `value` 는 양의 실수 |
| R-06 | 지원 단위 집합은 **등록된 단위**만 (초기: meter, feet, yard) |
| R-07 | 동적 등록: `1 <name> = <ratio> meter` → registry에 반영 |

---

## 6. 기능 요구사항

### 6.1 입력·파싱 (Boundary / U-IN)

| ID | 요구 | 판단 |
|----|------|------|
| FR-IN-01 | `:` 없음 | 거부 (E001) |
| FR-IN-02 | `value` 파싱 실패 | 거부 (E002) |
| FR-IN-03 | 미등록 `unit` | 거부 (E003) |
| FR-IN-04 | `value < 0` | 거부 (E004) |
| FR-IN-05 | 빈 문자열·공백만 | 거부 (E005) |
| FR-IN-06 | `unit:value` 정상 | `(unit, value)` 반환 |

### 6.2 환산 (Entity / D-CVT, D-REG, D-CFG)

| ID | 요구 | 판단 |
|----|------|------|
| FR-CVT-01 | 임의 등록 단위 → meter 기준값 | `to_base(unit, value)` |
| FR-CVT-02 | meter 기준값 → 대상 단위 | `from_base(unit, base)` |
| FR-CVT-03 | 한 입력에 **모든 등록 단위** 결과 | `convert_all(unit, value)` → `dict[str, float]` |
| FR-CVT-04 | feet/yard 상호 환산 | meter 경유, R-02·R-03·R-04 |
| FR-REG-01 | `register_unit(name, meters_per_unit)` | OCP — 기존 분기 수정 없이 추가 |
| FR-CFG-01 | JSON/YAML에서 비율 로드 | 파일 없으면 기본 3단위 |

### 6.3 출력 (Boundary / U-OUT)

| ID | 요구 | 판단 |
|----|------|------|
| FR-OUT-01 | 표 형태 (README 예시) | `{value} {unit} = {x} {other}` 줄 단위 |
| FR-OUT-02 | JSON | 키: 단위명, 값: 숫자 |
| FR-OUT-03 | CSV | 헤더 + 행 |

### 6.4 흐름 (Control)

| ID | 요구 | 판단 |
|----|------|------|
| FR-FLOW-01 | 파싱 → 검증 → 환산 → 포맷 | `control.flow.run_conversion` |

---

## 7. 성공 기준 (Mom Test · 품질)

| ID | 기준 | 연결 |
|----|------|------|
| SC-1 | `meter:2.5` 입력 시 feet·yard **수식 일치** (허용 오차 정의) | 증거 ① — 한 번에 전 단위 |
| SC-2 | 잘못된 입력 5종 **에러 코드** 기계 검증 | README 품질 요구 |
| SC-3 | cubit 등록 후 **동일 API**로 변환 가능 | 증거 ③ — 분기 증식 방지 |
| SC-4 | 비율 변경 시 **설정 파일만** 수정 (OCP) | 추가 요구사항 |
| SC-5 | RED → GREEN → REFACTOR **pytest 증거** | MagicSquare_XX 워크플로 |

---

## 8. C2C 추적 (요약)

| PRD | To-Do (인터페이스) | Test ID (RED) |
|-----|-------------------|---------------|
| FR-CVT-01 | `to_base("feet", 8.2021)` | D-CVT-01 |
| FR-CVT-03 | `convert_all("meter", 2.5)` | D-CVT-03 |
| FR-REG-01 | `register_unit("cubit", 0.4572)` | D-REG-01 |
| FR-IN-01 | `parse_input("meter2.5")` | U-IN-01 |
| FR-IN-04 | `validate` 음수 | U-IN-04 |
| FR-OUT-02 | `format_results(..., "json")` | U-OUT-02 |

상세 시나리오: [Report/03.UnitConverter_RED_TestPlan_Report.md](../Report/03.UnitConverter_RED_TestPlan_Report.md)  
인터페이스 시그니처: [INTERFACES.md](INTERFACES.md)

---

## 9. 아키텍처 원칙

- **ECB:** Entity(환산·등록) / Control(흐름) / Boundary(파싱·출력·설정 I/O)
- **Dual-Track TDD:** Logic Track (`D-*`) + UI Track (`U-*`)
- **RED 우선:** `tests/`만 · pytest **FAIL** → GREEN 최소 구현 → REFACTOR

### spec 브랜치 산출 (8계층 중)

| 계층 | 산출 |
|------|------|
| Rule | `.cursorrules` |
| Skill (예정) | `unit-converter-tdd` |
| Command (예정) | `/tdd-red`, `/review-ecb` |
| Test Loop | RED 설계표 · [TODO_RED.md](../TODO_RED.md) |

---

## 10. 용어

| 용어 | 정의 |
|------|------|
| 기준 단위(base) | meter — 모든 환산의 중간 표현 |
| meters_per_unit | `1 unit = k meter` 의 **k** |
| 등록 단위 | registry에 존재하는 단위 이름 |
| Logic Track | `D-*` — domain Mock 금지 |
| UI Track | `U-*` — boundary 중심, entity Mock 허용 |

---

## 11. 프로토타입 대비 갭 (`UnitConverter.py`)

| 항목 | 현재 코드 | PRD 목표 |
|------|-----------|----------|
| 구조 | `main()` 단일 함수 | ECB + SRP |
| OCP | `if unit == "meter"` 분기 | registry + converter |
| 음수 검증 | 없음 | E004 |
| 설정·동적 등록 | 하드코딩 상수 | FR-CFG-01, FR-REG-01 |
| 출력 포맷 | `print` 고정 | FR-OUT-01~03 |
| 테스트 | 없음 | Dual-Track pytest |
