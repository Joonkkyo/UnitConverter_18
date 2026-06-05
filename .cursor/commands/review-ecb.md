# ECB · 계약 리뷰

UnitConverter_18 **ECB·Dual-Track 계약** 정적 리뷰. **코드 수정 금지** — 위반만 표로 보고.

## 필수 선언

```text
Phase: review | Scope: src/ tests/ | Track: Logic|UI|both
```

- 헌법: `.cursorrules` · **Read/Grep만**

## 체크리스트 (5항목)

| # | 항목 | 기준 |
|---|------|------|
| 1 | **import 방향** | `boundary→control→entity` · entity가 boundary/control import **금지** · boundary가 entity import **금지** |
| 2 | **entity E001~E005** | entity에서 E00x **금지** |
| 3 | **ratio SSOT** | `3.28084`/`1.09361` → `entity.constants` 만 |
| 4 | **Logic Mock** | `tests/entity/`에서 patch/MagicMock **금지** |
| 5 | **control orchestration** | CLI·flow가 boundary→entity 순서 (control 경유) |

## Grep 예시

```bash
rg "from (boundary|control)" src/entity/
rg "from entity" src/boundary/
rg "E00[1-5]" src/entity/
rg "patch\\(" tests/entity/
```

## 금지

- 코드 수정 · commit (사용자 요청 시만)
