import json
import os
import re

def update_latest_week_readme():
    # 1. DORA 데이터 읽기
    try:
        with open('dora-report.json', 'r') as f:
            data = json.load(f)
            m = data['metrics']
            
        new_table = f"""
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | {m['deployment_frequency']} |
| Lead Time for Changes | {m['lead_time_for_changes']} |
| Change Failure Rate | {m['change_failure_rate']} |
| Time to Restore Service | {m['time_to_restore_service']} |
"""
    except Exception as e:
        print(f"데이터 에러: {e}")
        return

    # 2. weekX 폴더들 중 숫자가 가장 큰(최신) 폴더 찾기
    weeks = []
    for d in os.listdir("."):
        if os.path.isdir(d) and d.startswith("week"):
            match = re.search(r'week(\d+)', d)
            if match:
                weeks.append(int(match.group(1)))
    
    if not weeks:
        print("주차별 폴더를 찾을 수 없습니다.")
        return

    latest_week = f"week{max(weeks)}"
    target_path = os.path.join(latest_week, "README.md")

    # 3. 최신 주차 README만 업데이트
    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        start_marker = "<!-- START_DORA_METRICS -->"
        end_marker = "<!-- END_DORA_METRICS -->"

        if start_marker in content and end_marker in content:
            before = content.split(start_marker)[0]
            after = content.split(end_marker)[1]
            new_content = before + start_marker + new_table + end_marker + after
            
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 최신 주차({latest_week}) 리포트만 업데이트 완료!")
        else:
            print(f"⚠️ {latest_week} README에 마커가 없습니다.")
    else:
        print(f"❌ {target_path} 파일이 없습니다.")

if __name__ == "__main__":
    update_latest_week_readme()