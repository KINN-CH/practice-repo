# [Week 7] GitHub Actions 기반 기본 CI/CD 구축

## 1. 개요 (Overview)

GitHub Actions를 사용하여 코드 품질 자동 검증부터 배포까지 이어지는 완전한 CI/CD 파이프라인을 구축하였습니다.
Lint/Test 자동화, Matrix 전략을 통한 크로스 환경 검증, Secrets 기반 민감정보 주입, Build→Test→Deploy 의존성 파이프라인을 단계별로 구현합니다.

---

## 2. Mission 01 · 기본 CI 구축 (`ci.yml`)

| 항목 | 내용 |
| :--- | :--- |
| 트리거 | `on: push` (모든 브랜치) |
| Lint Job | `flake8 src/ tests/` |
| Test Job | `pytest tests/ -v` |
| 의존성 | `needs: lint` |
| 사용 액션 | `actions/checkout@v4`, `actions/setup-python@v5` |

**흐름**: `Push → lint (flake8) → test (pytest)`

---

## 3. Mission 02 · Matrix 빌드 (`matrix.yml`)

| 항목 | 내용 |
| :--- | :--- |
| OS | `ubuntu-latest`, `windows-latest` |
| Node 버전 | `16`, `18`, `20` |
| 병렬 Job 수 | 2 × 3 = **6개** |
| fail-fast | `false` |

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node-version: [16, 18, 20]
  fail-fast: false
```

---

## 4. Mission 03 · Build → Test → Deploy + Secrets (`deploy.yml`)

### 파이프라인 흐름

```
Build ──▶ Test ──▶ Deploy
  │          │          │
  └─ upload ─┘─ download┘  DEPLOY_TOKEN (Secret)
     artifact   artifact
```

### Job 구성

| Job | 조건 | 주요 작업 |
| :--- | :--- | :--- |
| Build | push/PR | lint → dist/ 패키징 → 아티팩트 업로드 |
| Test | `needs: build` | 아티팩트 다운로드 → Jest 테스트 |
| Deploy | `needs: test` + main 브랜치 | Secret 토큰으로 배포 |

### Secrets 설정

`Settings → Secrets and variables → Actions → New repository secret`

| Secret 이름 | 설명 |
| :--- | :--- |
| `DEPLOY_TOKEN` | 배포 서버 인증 토큰 |

---

## 5. 워크플로우 파일 목록

| 파일 | 역할 |
| :--- | :--- |
| `.github/workflows/ci.yml` | Python Lint + Test |
| `.github/workflows/matrix.yml` | Node.js Matrix 빌드 (6 Jobs) |
| `.github/workflows/deploy.yml` | Build → Test → Deploy |

---

## 6. Actions 실행 결과

- **CI Pipeline** — lint/test 2-Job 순차 실행 ✓
- **Matrix Build** — 6개 병렬 Job 동시 실행 ✓
- **Build → Test → Deploy** — 3-Job 체인, 아티팩트 전달, Secrets 주입 ✓
