# ADR 0001: DORA 지표 자동화를 위한 GitHub Actions 도입

## 상태 (Status)
Accepted (2026-03-18)

## 컨텍스트 (Context)
매주 수동으로 DORA 지표를 README에 기입하는 것은 번거롭고 실수할 확률이 높음.

## 결정 (Decision)
Python 스크립트(`update_all_readmes.py`)와 GitHub Actions를 연동하여 푸시 시 자동으로 모든 주차의 README를 갱신하도록 함.

## 결과 (Consequences)
- 장점: 데이터 일관성 유지, 문서화 공수 감소.
- 단점: 워크플로우 실행 시간에 따른 약간의 지연 발생.