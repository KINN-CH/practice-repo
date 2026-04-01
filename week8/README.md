# [Week 8] 워크플로우 실행 최적화 (재사용 / 캐싱 / 조건부)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 1. 개요 (Overview)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
기존 CI/CD 파이프라인의 세 가지 문제를 해결합니다.
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 문제 | 해결책 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :--- |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 워크플로우마다 checkout/setup 단계 반복 | **Composite Action** + **Reusable Workflow** 로 중복 제거 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 매 push마다 불필요한 의존성 재설치 | **actions/cache** 로 npm · pip 캐싱 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 관련 없는 파일 변경에도 전체 파이프라인 실행 | **paths 필터** + **if 조건** 으로 선택적 실행 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 2. Matrix 확장 (3 OS × 3 Node = 9개 병렬 Job)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
Week 07의 `2 OS × 3 Node(16/18/20)` → `3 OS × 3 Node(18/20/22)` 로 확장
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
strategy:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  matrix:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    os: [ubuntu-latest, windows-latest, macos-latest]
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    node-version: ['18', '20', '22']
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  fail-fast: false
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| | ubuntu-latest | windows-latest | macos-latest |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :---: | :---: | :---: | :---: |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Node 18** | ✓ | ✓ | ✓ |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Node 20** | ✓ | ✓ | ✓ |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Node 22** | ✓ | ✓ | ✓ |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> Node 16은 EOL(2023-09) 종료로 22로 교체
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 3. Reusable Workflow + Composite Action
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### 구조
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
matrix.yml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  └─ uses: reusable-test.yml          ← Reusable Workflow (workflow_call)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
       └─ uses: setup-node-env        ← Composite Action
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
            ├─ actions/checkout@v4
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
            ├─ actions/setup-node@v4
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
            ├─ actions/cache@v4 (npm)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
            └─ npm install
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### Composite Action (`.github/actions/setup-node-env/action.yml`)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
3개 워크플로우에서 반복되던 4단계(checkout → setup-node → cache → install)를 단일 액션으로 통합:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
inputs:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  node-version:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    default: '20'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
runs:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  using: 'composite'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  steps:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    - uses: actions/checkout@v4
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    - uses: actions/setup-node@v4
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      with:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        node-version: ${{ inputs.node-version }}
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    - uses: actions/cache@v4
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      with:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        path: ~/.npm
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        key: ${{ runner.os }}-node${{ inputs.node-version }}-${{ hashFiles('package.json') }}
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    - run: npm install
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      shell: bash
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### Reusable Workflow (`.github/workflows/reusable-test.yml`)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
`workflow_call` 트리거로 다른 워크플로우에서 호출 가능:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
on:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  workflow_call:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    inputs:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      os:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        type: string
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        default: 'ubuntu-latest'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      node-version:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        type: string
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        default: '20'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
matrix.yml에서 호출:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
jobs:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  matrix-test:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    strategy:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      matrix:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        os: [ubuntu-latest, windows-latest, macos-latest]
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
        node-version: ['18', '20', '22']
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    uses: KINN-CH/practice-repo/.github/workflows/reusable-test.yml@main
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    with:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      os: ${{ matrix.os }}
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      node-version: ${{ matrix.node-version }}
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 4. 캐싱 전후 실행 시간 비교
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### 4-1. CI Pipeline (Python / pip 캐시)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
측정 조건: `ubuntu-latest`, Python 3.10, `flake8` + `pytest` + `pandas` 등
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| Job | 캐시 없음 (Week 07) | Cold Cache (첫 실행) | Warm Cache (두 번째 실행) | 개선률 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :---: | :---: | :---: | :---: |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| Lint (flake8) | 6s | 7s | 7s | — |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| Test (pytest) | 26s | 26s | 27s | — |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **합계** | **32s** | **33s** | **34s** | — |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> **분석**: pip 패키지 수가 적어(flake8, pytest, pandas 등 5개) 캐시 효과보다 캐시 키 계산 오버헤드가 큰 상황.  
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> 의존성이 수십 개 이상인 실제 프로젝트에서는 `pip install` 시간(20~60s)이 캐시로 2~3s로 단축됩니다.
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
캐시 적용 방법:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
- uses: actions/setup-python@v5
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  with:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    python-version: "3.10"
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    cache: 'pip'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    cache-dependency-path: requirements.txt
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### 4-2. Matrix Build (Node.js / npm 캐시)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
#### Cold Cache (Week 08 첫 번째 실행)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| OS | Node 18 | Node 20 | Node 22 | 평균 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :---: | :---: | :---: | :---: |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| ubuntu | 24s | 20s | 20s | **21s** |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| windows | 45s | 40s | 58s | **48s** |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| macos | 39s | 30s | 25s | **31s** |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
#### Warm Cache (Week 08 두 번째 실행)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| OS | Node 18 | Node 20 | Node 22 | 평균 | 개선률 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| ubuntu | 20s | 13s | 19s | **17s** | ▼ **19%** |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| windows | 41s | 49s | 68s | **53s** | — |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| macos | 31s | 16s | 29s | **25s** | ▼ **19%** |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> **분석**:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> - **ubuntu · macOS**: npm 캐시 HIT 확인, 평균 19% 단축
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> - **windows**: npm 캐시 경로(`~/.npm`) 접근이 Linux 대비 느리고 I/O 오버헤드로 편차 큼
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
> - npm 패키지가 많은 실제 프로젝트(`node_modules` 수백 MB)에서는 30~60% 단축 효과
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 5. 조건부 실행 (paths 필터 + if 조건)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### 5-1. paths 필터 — 관련 파일 변경 시만 실행
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 워크플로우 | 실행 조건 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :--- |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| `ci.yml` | `src/**`, `tests/**`, `requirements.txt` 변경 시 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| `matrix.yml` | `src/**`, `tests/**`, `package.json` 변경 시 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| `deploy.yml` | `src/**`, `package.json`, `requirements.txt` 변경 시 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
on:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  push:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    paths:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      - 'src/**'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      - 'tests/**'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      - 'requirements.txt'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
**효과**: README, week*/  등 문서만 변경할 경우 CI 파이프라인 전혀 실행되지 않음  
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
→ 불필요한 실행 **100% 차단**, GitHub Actions 분 절약
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
### 5-2. if 조건 — main 브랜치 push일 때만 배포
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```yaml
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
deploy:
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  needs: test
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
PR 빌드에서는 Build/Test만 실행, Deploy는 건너뜀
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 6. 파일 구조 요약
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
.github/
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  actions/
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    setup-node-env/
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
      action.yml          ← Composite Action (checkout+setup+cache+install)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  workflows/
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    ci.yml                ← Python lint/test + pip cache + paths 필터
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    matrix.yml            ← 9개 병렬 Job (3 OS × 3 Node) + Reusable 호출
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    reusable-test.yml     ← Reusable Workflow (workflow_call)
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    deploy.yml            ← Build→Test→Deploy + npm cache + 조건부 배포
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
    metrics.yml           ← DORA 메트릭 수집
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
week8/
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
  README.md               ← 본 문서
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
```
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
---
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
## 7. 최적화 효과 종합
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |

| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| 최적화 항목 | 적용 전 | 적용 후 | 효과 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| :--- | :--- | :--- | :--- |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Composite Action** | 워크플로우마다 4단계 반복 | 1줄 `uses` 호출 | 중복 코드 제거 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Reusable Workflow** | matrix.yml에 전체 steps 기술 | `uses: .yml@main` 한 줄 | 워크플로우 재사용 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **npm 캐시** | 매번 npm install (20~60s) | 캐시 HIT 시 2~5s | ubuntu/macOS 19% 단축 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **pip 캐시** | 매번 pip install | 캐시 HIT 시 즉시 | 대규모 프로젝트 효과 큼 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **paths 필터** | 모든 push에서 전체 실행 | 관련 파일 변경 시만 실행 | 불필요 실행 100% 차단 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **if 조건** | PR에서도 deploy 실행 | main push에서만 deploy | 의도치 않은 배포 방지 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
| **Matrix 확장** | 2 OS × 3 Node = 6 Jobs | 3 OS × 3 Node = 9 Jobs | macOS 커버리지 추가 |
| 지표 (Metric) | 수치 (Value) |
| :--- | :--- |
| Deployment Frequency | 1.0/day |
| Lead Time for Changes | 45m |
| Change Failure Rate | 0% |
| Time to Restore Service | 12m |
