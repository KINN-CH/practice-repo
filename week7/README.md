# [Week 7] GitHub Actions 기반 기본 CI/CD 구축

## 1. 개요 (Overview)

GitHub Actions를 사용하여 코드 품질 자동 검증부터 배포까지 이어지는 완전한 CI/CD 파이프라인을 구축하였습니다.  
Lint/Test 자동화, Matrix 전략을 통한 크로스 환경 검증, Secrets 기반 민감정보 주입, Build→Test→Deploy 의존성 파이프라인을 단계별로 구현합니다.

---

## 2. 구현 항목

### Mission 01 · 기본 CI 구축 (`ci.yml`)

> **목표**: 코드 Push 시 Lint와 Test를 자동 실행하는 기본 파이프라인

| 항목 | 내용 |
| :--- | :--- |
| 트리거 | `on: push` (모든 브랜치) |
| Lint Job | `flake8 src/ tests/` — Python 코드 스타일 검사 |
| Test Job | `pytest tests/ -v` — 단위 테스트 5개 실행 |
| 의존성 | `needs: lint` — Lint 통과 후 Test 실행 |
| 사용 액션 | `actions/checkout@v4`, `actions/setup-python@v5` |

**파이프라인 흐름**

```
Push → lint (flake8) ──성공──▶ test (pytest)
```

**핵심 파일**
- `.github/workflows/ci.yml`
- `src/calculator.py` — 테스트 대상 모듈
- `tests/test_calculator.py` — pytest 단위 테스트

---

### Mission 02 · Matrix 빌드 (`matrix.yml`)

> **목표**: 하나의 설정으로 여러 OS × Node.js 버전 조합을 병렬 테스트

| 항목 | 내용 |
| :--- | :--- |
| OS 매트릭스 | `ubuntu-latest`, `windows-latest` |
| 버전 매트릭스 | Node.js `16`, `18`, `20` |
| 병렬 Job 수 | 2 OS × 3 버전 = **6개 병렬 Job** |
| fail-fast | `false` — 하나 실패해도 전체 결과 수집 |
| 사용 액션 | `actions/checkout@v4`, `actions/setup-node@v4` |

**매트릭스 조합**

| | ubuntu-latest | windows-latest |
| :---: | :---: | :---: |
| **Node 16** | ✓ | ✓ |
| **Node 18** | ✓ | ✓ |
| **Node 20** | ✓ | ✓ |

**핵심 설정**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node-version: [16, 18, 20]
  fail-fast: false

runs-on: ${{ matrix.os }}
node-version: ${{ matrix.node-version }}
```

**핵심 파일**
- `.github/workflows/matrix.yml`
- `src/calculator.js` — 테스트 대상 모듈 (Node.js)
- `tests/calculator.test.js` — Jest 단위 테스트

---

### Mission 03 · Build → Test → Deploy + Secrets (`deploy.yml`)

> **목표**: Job 간 의존성과 아티팩트 전달, Secrets 기반 배포 파이프라인

#### 3-1. 파이프라인 흐름

```
Build ──▶ Test ──▶ Deploy
  │          │          │
  │  아티팩트  │  아티팩트  │  DEPLOY_TOKEN
  └─ upload ─┘─ download ┘  (GitHub Secret)
```

#### 3-2. Job 구성

| Job | 조건 | 주요 작업 |
| :--- | :--- | :--- |
| **Build** | push/PR | lint → dist/ 패키징 → 아티팩트 업로드 |
| **Test** | `needs: build` | 아티팩트 다운로드 → Jest 테스트 실행 |
| **Deploy** | `needs: test` + `main` 브랜치 | 아티팩트 다운로드 → Secret 토큰으로 배포 |

#### 3-3. 아티팩트 업로드 / 다운로드

```yaml
# Build Job — 아티팩트 업로드
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7

# Test / Deploy Job — 아티팩트 다운로드
- uses: actions/download-artifact@v4
  with:
    name: build-output
    path: dist/
```

#### 3-4. Secrets 설정 방법

GitHub 저장소 → **Settings → Secrets and variables → Actions → New repository secret**

| Secret 이름 | 설명 |
| :--- | :--- |
| `DEPLOY_TOKEN` | 배포 서버 인증 토큰 (예: API Key) |

워크플로우에서 참조:

```yaml
env:
  DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

> **주의**: Secret 값은 로그에 절대 출력되지 않으며, `***`로 마스킹됩니다.

---

## 3. 워크플로우 파일 목록

| 파일 | 역할 | 트리거 |
| :--- | :--- | :--- |
| `.github/workflows/ci.yml` | Python Lint + Test | 모든 브랜치 push |
| `.github/workflows/matrix.yml` | Node.js Matrix 빌드 | 모든 브랜치 push |
| `.github/workflows/deploy.yml` | Build → Test → Deploy | main 브랜치 push |
| `.github/workflows/metrics.yml` | DORA 메트릭 수집 | main 브랜치 push |

---

## 4. Actions 실행 결과 확인

저장소 상단 **Actions 탭** 에서 아래 항목을 확인할 수 있습니다.

- **CI Pipeline** — Lint/Test 2-Job 순차 실행, 녹색 체크
- **Matrix Build** — 6개 병렬 Job (2 OS × 3 Node 버전) 동시 실행
- **Build → Test → Deploy** — 3-Job 의존성 체인, 아티팩트 전달, Secrets 주입

---

## 5. 기술 스택

| 구분 | 도구 |
| :--- | :--- |
| CI/CD | GitHub Actions |
| Python Lint | flake8 |
| Python Test | pytest |
| JS Lint | ESLint |
| JS Test | Jest |
| 아티팩트 | actions/upload-artifact@v4 / download-artifact@v4 |
| 언어 설정 | actions/setup-python@v5, actions/setup-node@v4 |
