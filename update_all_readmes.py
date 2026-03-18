import json
import os
import re

def update_latest_week_readme():
    try:
        with open('dora-report.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            m = data['metrics']
        
        # 주입할 표 내용 (딱 4줄만!)
        new_lines = [
            "| 지표 (Metric) | 수치 (Value) |\n",
            "| :--- | :--- |\n",
            f"| Deployment Frequency | {m['deployment_frequency']} |\n",
            f"| Lead Time for Changes | {m['lead_time_for_changes']} |\n",
            f"| Change Failure Rate | {m['change_failure_rate']} |\n",
            f"| Time to Restore Service | {m['time_to_restore_service']} |\n"
        ]
    except Exception as e:
        print(f"Error: {e}")
        return

    weeks = [int(re.search(r'week(\d+)', d).group(1)) for d in os.listdir(".") if os.path.isdir(d) and re.search(r'week(\d+)', d)]
    if not weeks: return
    latest_week = f"week{max(weeks)}"
    target_path = os.path.join(latest_week, "README.md")

    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        updated_lines = []
        skip = False
        for line in lines:
            if "" in line:
                updated_lines.append(line)
                updated_lines.extend(new_lines) # 표 삽입
                skip = True # 마커 사이 내용은 건너뜀
            elif "" in line:
                updated_lines.append(line)
                skip = False
            elif not skip:
                updated_lines.append(line)

        with open(target_path, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print(f"Success: {latest_week}/README.md updated!")
    else:
        print("File not found.")

if __name__ == "__main__":
    update_latest_week_readme()