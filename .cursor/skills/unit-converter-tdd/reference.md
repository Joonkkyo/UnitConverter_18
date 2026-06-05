# Test ID SSOT — UnitConverter_18

> Report 코드명 `UnitConverter_XX`와 동일 Test ID. 패키지: `unit-converter-18`.

> 연계: [docs/PRD.md](../../../docs/PRD.md) · [Report/03](../../../Report/03.UnitConverter_RED_TestPlan_Report.md)

## Logic Track — D-*

| ID | PRD | 요약 | 파일 (예정) |
|----|-----|------|-------------|
| D-CVT-01 | FR-CVT-01 | feet ↔ meter round-trip | `test_d_cvt_01.py` |
| D-CVT-02 | FR-CVT-04 | yard ↔ meter | `test_d_cvt_02.py` ✅ |
| D-CVT-03 | FR-CVT-03 | `convert_all("meter", 2.5)` | `test_d_cvt_03.py` |
| D-REG-01 | FR-REG-01 | `register_unit("cubit", …)` | `test_d_reg_01.py` |
| D-REG-02 | FR-REG-01 | 중복 등록 거부 | `test_d_reg_02.py` |
| D-CFG-01 | FR-CFG-01 | 설정 파일 로드 | `test_d_cfg_01.py` |

## UI Track — U-*

| ID | PRD | 요약 | 파일 (예정) |
|----|-----|------|-------------|
| U-IN-01 | FR-IN-01 | 콜론 없음 → E001 | `test_u_in_01.py` |
| U-IN-02 | FR-IN-02 | 잘못된 숫자 → E002 | `test_u_in_02.py` |
| U-IN-03 | FR-IN-03 | 미지원 단위 → E003 | `test_u_in_03.py` |
| U-IN-04 | FR-IN-04 | 음수 → E004 | `test_u_in_04.py` |
| U-IN-05 | FR-IN-05 | 빈 입력 → E005 | `test_u_in_05.py` |
| U-OUT-01 | FR-OUT-01 | 표 형식 (1자리) | `test_u_out_01.py` |
| U-OUT-02 | FR-OUT-02 | JSON | `test_u_out_02.py` |
| U-OUT-03 | FR-OUT-03 | CSV | `test_u_out_03.py` |
| U-FLOW-01 | FR-FLOW-01 | `run_conversion` 성공 | `test_u_flow_01.py` ✅ |
| U-FLOW-02 | FR-FLOW-01 | 검증 실패 시 convert_all 미호출 | `test_u_flow_02.py` ✅ |
| U-OUT-01 | FR-OUT-01 | 표 1자리 반올림 | `test_u_out_01.py` ✅ |

파일명: `tests/entity/test_d_<slug>.py` · `tests/boundary/test_u_<slug>.py`
