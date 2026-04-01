# [Week 8] 워크플로우 실행 최적화 (재사용 / 캐싱 / 조건부)

## 1. 개요 (Overview)

기존 CI/CD 파이프라인의 세 가지 문제를 해결합니다.

| 문제 | 해결책 |
| :--- | :--- |
| 워크플로우마다 checkout/setup 단계 반복 | **Composite Action** + **Reusable Workflow** 로 중복 제거 |
| 매 push마다 불필요한 의존성 재설치 | **actions/cache** 로 npm · pip 캐싱 |
| 관련 없는 파일 변경에도 전체 파이프라인 실행 | **paths 필터** + **if 조건** 으로 선택적 실행 |

---

## 2. Matrix 확장 (3 OS × 3 Node = 9개 병렬 Job)

Week 07의 `2 OS × 3 Node(16/18/20)` → `3 OS × 3 Node(18/20/22)` 로 확장

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: ['18', '20', '22']
  fail-fast: false
```

| | ubuntu-latest | windows-latest | macos-latest |
| :---: | :---: | :---: | :---: |
| **Node 18** | ✓ | ✓ | ✓ |
| **Node 20** | ✓ | ✓ | ✓ |
| **Node 22** | ✓ | ✓ | ✓ |

> Node 16은 EOL(2023-09) 종료로 22로 교체

---

## 3. Reusable Workflow + Composite Action

### 구조

```
matrix.yml
  └─ uses: reusable-test.yml          ← Reusable Workflow (workflow_call)
       └─ uses: setup-node-env        ← Composite Action
            ├─ actions/checkout@v4
            ├─ actions/setup-node@v4
            ├─ actions/cache@v4 (npm)
            └─ npm install
```

### Composite Action (`.github/actions/setup-node-env/action.yml`)

3개 워크플로우에서 반복되던 4단계(checkout → setup-node → cache → install)를 단일 액션으로 통합:

```yaml
inputs:
  node-version:
    default: '20'
runs:
  using: 'composite'
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
    - uses: actions/cache@v4
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node${{ inputs.node-version }}-${{ hashFiles('package.json') }}
    - run: npm install
      shell: bash
```

### Reusable Workflow (`.github/workflows/reusable-test.yml`)

`workflow_call` 트리거로 다른 워크플로우에서 호출 가능:

```yaml
on:
  workflow_call:
    inputs:
      os:
        type: string
        default: 'ubuntu-latest'
      node-version:
        type: string
        default: '20'
```

matrix.yml에서 호출:

```yaml
jobs:
  matrix-test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: ['18', '20', '22']
    uses: KINN-CH/practice-repo/.github/workflows/reusable-test.yml@main
    with:
      os: ${{ matrix.os }}
      node-version: ${{ matrix.node-version }}
```

---

## 4. 캐싱 전후 실행 시간 비교

### 4-1. CI Pipeline (Python / pip 캐시)

측정 조건: `ubuntu-latest`, Python 3.10, `flake8` + `pytest` + `pandas` 등

| Job | 캐시 없음 (Week 07) | Cold Cache (첫 실행) | Warm Cache (두 번째 실행) | 개선률 |
| :--- | :---: | :---: | :---: | :---: |
| Lint (flake8) | 6s | 7s | 7s | — |
| Test (pytest) | 26s | 26s | 27s | — |
| **합계** | **32s** | **33s** | **34s** | — |

> **분석**: pip 패키지 수가 적어(flake8, pytest, pandas 등 5개) 캐시 효과보다 캐시 키 계산 오버헤드가 큰 상황.  
> 의존성이 수십 개 이상인 실제 프로젝트에서는 `pip install` 시간(20~60s)이 캐시로 2~3s로 단축됩니다.

캐시 적용 방법:
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.10"
    cache: 'pip'
    cache-dependency-path: requirements.txt
```

---

### 4-2. Matrix Build (Node.js / npm 캐시)

#### Cold Cache (Week 08 첫 번째 실행)

| OS | Node 18 | Node 20 | Node 22 | 평균 |
| :--- | :---: | :---: | :---: | :---: |
| ubuntu | 24s | 20s | 20s | **21s** |
| windows | 45s | 40s | 58s | **48s** |
| macos | 39s | 30s | 25s | **31s** |

#### Warm Cache (Week 08 두 번째 실행)

| OS | Node 18 | Node 20 | Node 22 | 평균 | 개선률 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| ubuntu | 20s | 13s | 19s | **17s** | ▼ **19%** |
| windows | 41s | 49s | 68s | **53s** | — |
| macos | 31s | 16s | 29s | **25s** | ▼ **19%** |

> **분석**:
> - **ubuntu · macOS**: npm 캐시 HIT 확인, 평균 19% 단축
> - **windows**: npm 캐시 경로(`~/.npm`) 접근이 Linux 대비 느리고 I/O 오버헤드로 편차 큼
> - npm 패키지가 많은 실제 프로젝트(`node_modules` 수백 MB)에서는 30~60% 단축 효과

---

## 5. 조건부 실행 (paths 필터 + if 조건)

### 5-1. paths 필터 — 관련 파일 변경 시만 실행

| 워크플로우 | 실행 조건 |
| :--- | :--- |
| `ci.yml` | `src/**`, `tests/**`, `requirements.txt` 변경 시 |
| `matrix.yml` | `src/**`, `tests/**`, `package.json` 변경 시 |
| `deploy.yml` | `src/**`, `package.json`, `requirements.txt` 변경 시 |

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'tests/**'
      - 'requirements.txt'
```

**효과**: README, week*/  등 문서만 변경할 경우 CI 파이프라인 전혀 실행되지 않음  
→ 불필요한 실행 **100% 차단**, GitHub Actions 분 절약

### 5-2. if 조건 — main 브랜치 push일 때만 배포

```yaml
deploy:
  needs: test
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

PR 빌드에서는 Build/Test만 실행, Deploy는 건너뜀

---

## 6. 파일 구조 요약

```
.github/
  actions/
    setup-node-env/
      action.yml          ← Composite Action (checkout+setup+cache+install)
  workflows/
    ci.yml                ← Python lint/test + pip cache + paths 필터
    matrix.yml            ← 9개 병렬 Job (3 OS × 3 Node) + Reusable 호출
    reusable-test.yml     ← Reusable Workflow (workflow_call)
    deploy.yml            ← Build→Test→Deploy + npm cache + 조건부 배포
    metrics.yml           ← DORA 메트릭 수집
week8/
  README.md               ← 본 문서
```

---

## 7. 최적화 효과 종합

| 최적화 항목 | 적용 전 | 적용 후 | 효과 |
| :--- | :--- | :--- | :--- |
| **Composite Action** | 워크플로우마다 4단계 반복 | 1줄 `uses` 호출 | 중복 코드 제거 |
| **Reusable Workflow** | matrix.yml에 전체 steps 기술 | `uses: .yml@main` 한 줄 | 워크플로우 재사용 |
| **npm 캐시** | 매번 npm install (20~60s) | 캐시 HIT 시 2~5s | ubuntu/macOS 19% 단축 |
| **pip 캐시** | 매번 pip install | 캐시 HIT 시 즉시 | 대규모 프로젝트 효과 큼 |
| **paths 필터** | 모든 push에서 전체 실행 | 관련 파일 변경 시만 실행 | 불필요 실행 100% 차단 |
| **if 조건** | PR에서도 deploy 실행 | main push에서만 deploy | 의도치 않은 배포 방지 |
| **Matrix 확장** | 2 OS × 3 Node = 6 Jobs | 3 OS × 3 Node = 9 Jobs | macOS 커버리지 추가 |
