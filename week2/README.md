# [2주차] DORA 메트릭 수집 자동화
> 본 문서는 생성형 AI(Gemini)의 도움을 받아 작성되었으며, 과제 요구사항에 따라 DORA 지표 수집 체계를 기술합니다.

## 1. DORA 4대 지표 수집 개요
프로젝트의 성능과 효율성을 측정하기 위해 GitHub Actions를 활용하여 아래 4대 지표를 자동 수집합니다.
- Deployment Frequency: 배포 빈도
- Lead Time for Changes: 변경 리드 타임
- Change Failure Rate: 변경 실패율
- Time to Restore Service: 서비스 복구 시간

## 2. 수집 자동화 구현 (GitHub Actions)
- 워크플로우 파일: .github/workflows/metrics.yml
- 수집 방식: push 이벤트 발생 시마다 Python 환경을 구성하여 지표를 계산하고 dora-report.json으로 저장합니다.
- 아티팩트 관리: 수집된 JSON 데이터는 GitHub Actions Artifact로 보관되어 데이터의 연속성을 보장합니다.

## 3. DORA Metrics 대시보드 시안 및 구현 결과

<!-- START_METRICS_TABLE -->
| 지표 (Metric) | 수치 (Value) | 상태 (Status) |
| :--- | :--- | :--- |
| Deployment Frequency | 1.0/day | High |
| Lead Time for Changes | 45m | Elite |
| Change Failure Rate | 0% | Elite |
| Time to Restore Service | 12m | Elite |
<!-- END_METRICS_TABLE -->
---
## 선택 과제 수행 내역
- JSON 아티팩트 저장: 워크플로우 실행 완료 후 dora-report.json 파일을 다운로드 가능하도록 구성하였습니다.
- 주간 보고서 자동 생성: Actions 실행 로그를 통해 수집 결과를 텍스트 리포트 형태로 상시 출력합니다.