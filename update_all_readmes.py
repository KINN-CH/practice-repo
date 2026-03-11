import json
import os

# 1. JSON 데이터 읽기
with open('dora-report.json', 'r') as f:
    data = json.load(f)

metrics = data['metrics']

# 2. 업데이트할 표 내용 생성
new_table = f"""
| 지표 (Metric) | 수치 (Value) | 상태 (Status) |
| :--- | :--- | :--- |
| Deployment Frequency | {metrics['deployment_frequency']} | High |
| Lead Time for Changes | {metrics['lead_time_for_changes']} | Elite |
| Change Failure Rate | {metrics['change_failure_rate']} | Elite |
| Time to Restore Service | {metrics['time_to_restore_service']} | Elite |
"""

# 3. README.md 파일 읽고 표 부분 교체
readme_path = 'week2/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 표가 들어갈 위치를 지정 (주석 태그 활용)
start_marker = "<!-- START_METRICS_TABLE -->"
end_marker = "<!-- END_METRICS_TABLE -->"

if start_marker in content and end_marker in content:
    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]
    new_content = before + start_marker + new_table + end_marker + after
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)