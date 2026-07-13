# 파이썬 데이터 분석 & PLC 자동화 연계 학습 노트

## 1. 파이썬 데이터 분석 핵심 패키지

### NumPy
수치 연산의 기반이 되는 라이브러리. 배열(array) 단위의 벡터화 연산을 빠르게 처리하며, Pandas를 포함한 대부분의 분석 라이브러리가 내부적으로 NumPy 기반으로 동작한다.

```python
import numpy as np
pressure = np.array([101.2, 102.5, 99.8, 103.1, 100.4])
print(f"평균 압력: {pressure.mean():.2f}")
print(f"최대 편차: {pressure.max() - pressure.min():.2f}")
```

### Pandas
표(DataFrame) 형태로 데이터를 다루는 분석의 핵심 도구. CSV/Excel 불러오기, 결측치 처리, groupby 집계, merge/concat 등을 지원한다.

```python
import pandas as pd
df = pd.DataFrame({
    '설비ID': ['M01', 'M02', 'M01', 'M03', 'M02'],
    '가동시간': [120, 95, 130, 80, 110],
    '불량여부': [0, 1, 0, 0, 1]
})
result = df.groupby('설비ID').agg(
    평균가동시간=('가동시간', 'mean'),
    불량건수=('불량여부', 'sum')
)
```

### Matplotlib / Seaborn / Plotly / Dash
- **Matplotlib**: 모든 시각화의 기초. 세밀한 조절이 가능하나 코드가 길고 디자인이 투박함. 논문·학술 보고서에 적합.
- **Seaborn**: Matplotlib 기반, Pandas와 강하게 연동. 한 줄로 세련된 통계 그래프 작성 가능. EDA·블로그에 적합.
- **Plotly**: 줌/호버 등 인터랙티브 그래프. HTML로 바로 공유 가능. 발표·웹 리포트에 적합.
- **Dash**: Plotly 기반, 파이썬만으로 웹 대시보드 구축.

### Scikit-learn (머신러닝 기초)
- **회귀(Regression)**: 숫자를 예측 (예: 가동시간 → 전력소비량)
- **분류(Classification)**: 카테고리를 예측 (예: 양품/불량 판정)

```python
from sklearn.linear_model import LinearRegression
X = df[['가동시간']]
y = df['불량여부']
model = LinearRegression()
model.fit(X, y)
print(model.predict([[100]]))
```

핵심 워크플로우: 데이터 준비 → 학습용/테스트용 분리 → 모델 학습 → 예측 → 성능 평가

주요 알고리즘 난이도 순: 선형/로지스틱 회귀 → 의사결정나무 → 랜덤포레스트 → KNN → 딥러닝

---

## 2. 목적별 파이썬 패키지 로드맵

| 분야 | 핵심 패키지 | 요약 |
|---|---|---|
| 게임 개발 | Pygame | 그래픽/사운드/이벤트 루프 기반 2D 게임 제작 |
| 데이터 시각화 | Matplotlib, Seaborn, Plotly, Dash | 정적 → 통계 → 인터랙티브 → 웹 대시보드 |
| 웹 개발 | Django, Flask, FastAPI | 올인원 vs 미니멀 vs 고성능 비동기 |
| 자동화/크롤링 | Requests, Selenium | API 통신 vs 브라우저 상호작용 |

### 웹 프레임워크 비교

| 항목 | Django | Flask | FastAPI |
|---|---|---|---|
| 철학 | 풀스택 (배터리 포함) | 마이크로 (BYOE) | 현대적 API (비동기) |
| 학습 곡선 | 가파름 | 낮음 | 중간 |
| 성능 | 양호 (WSGI) | 보통 (WSGI) | 최고 (ASGI 비동기) |
| 추천 상황 | 대규모 상용 서비스 | 소규모 실험/MVP | 고성능 API 서버 |

---

## 3. 파이썬 함수 (Function)

반복되는 코드를 이름으로 묶어 재사용하는 도구. PLC의 서브루틴과 유사한 개념.

```python
def 압력_체크(압력, 기준값=100):
    if 압력 > 기준값:
        return "경고"
    return "정상"
```

- 기본값 매개변수, 여러 값 반환, `*args` 가변 인자, 람다 함수(`lambda x: x**2`) 등을 다룸
- 함수 분리의 이유: 코드 재사용성, 디버깅 용이성, 단위 테스트 가능

---

## 4. 파일 입출력 (File I/O)

`with` 구문으로 파일을 안전하게 열고 자동으로 닫는다.

```python
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("설비 가동 시작\n")
```

- 모드: `r`(읽기), `w`(쓰기/덮어쓰기), `a`(이어쓰기), `r+`(읽기+쓰기)
- CSV: `csv` 모듈 또는 Pandas의 `read_csv`/`to_csv`
- JSON: 설정값 저장에 유용 (`json.dump`, `json.load`)
- 예외 처리 필수: `try/except FileNotFoundError` 등으로 방어

```python
import csv, datetime
def 로그_저장(파일명, 시간, 사이클타임, 이상여부):
    with open(파일명, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([시간, 사이클타임, '이상' if 이상여부 else '정상'])
```

---

## 5. 클래스 (Class) — PLC 함수블록(FB)과의 연계

클래스는 설비 하나가 가진 상태값(온도, 압력, 가동시간)과 동작(시작, 정지, 체크)을 하나로 묶는 설계도. **PLC의 함수블록(FB)과 동일한 사고방식** — FB로 실린더 하나의 동작을 템플릿화해 여러 실린더에 재사용하듯, 클래스로 설비 하나의 틀을 만들어 여러 인스턴스에 재사용한다.

```python
class 설비:
    def __init__(self, 설비ID, 기준압력=100):
        self.설비ID = 설비ID
        self.기준압력 = 기준압력
        self.가동중 = False

    def 시작(self):
        self.가동중 = True

    def 압력체크(self, 현재압력):
        if 현재압력 > self.기준압력:
            return f"{self.설비ID} 경고"
        return f"{self.설비ID} 정상"

M01 = 설비('M01', 기준압력=100)
M02 = 설비('M02', 기준압력=120)
```

**상속** — 공통 기능은 부모 클래스에, 다른 부분만 자식 클래스에서 재정의 (예: 실린더 → 양솔실린더)

---

## 6. 모듈 (Module) — PLC 프로그램 블록 구성과의 연계

기능별로 파일을 나누는 것. **PLC 프로그램을 공통/스텝제어/알람 등 블록 단위로 나누는 것과 동일한 개념.**

```
project/
├── main.py
├── equipment.py      # 설비 클래스
├── plc_comm.py        # PLC 통신 함수
└── logger.py           # 로그 저장 함수
```

```python
# main.py
from equipment import 설비
from logger import 로그_저장

M01 = 설비('M01', 기준압력=100)
상태 = M01.압력체크(105)
로그_저장('log.csv', 'M01', 상태)
```

패키지(모듈들의 폴더 묶음)로 더 큰 프로젝트를 구성할 수도 있다.

---

## 7. 파이썬 ↔ PLC 실제 통신 (pymcprotocol)

미쓰비시 PLC와 통신하는 대표적 방법은 **MC프로토콜**. 이더넷 포트를 통해 D레지스터, M코일 값을 읽고 쓴다.

**사전 준비 (GX Works2 측)**
- PLC 파라미터에서 이더넷 포트 설정 (IP주소, 포트번호)
- MC프로토콜 통신 허용을 위한 오픈 설정(Open Setting)
- 방화벽/네트워크 포트 접근 허용

**설치**
```bash
pip install pymcprotocol
```

**기본 사용법**
```python
import pymcprotocol

plc = pymcprotocol.Type3E()  # 이더넷 3E프레임
plc.connect('192.168.1.10', 5000)

# D레지스터 읽기
결과 = plc.batchread_wordunits(headdevice='D100', readsize=5)

# M코일 읽기
비트결과 = plc.batchread_bitunits(headdevice='M0', readsize=10)

# D레지스터 쓰기
plc.batchwrite_wordunits(headdevice='D200', values=[123])

# M코일 쓰기
plc.batchwrite_bitunits(headdevice='M10', values=[1])

plc.close()
```

**실무 주의사항**
| 항목 | 설명 |
|---|---|
| 예외 처리 필수 | 네트워크 끊김, 타임아웃 등 실제로 자주 발생 |
| 폴링 주기 | 너무 자주 읽으면 PLC 부하 발생 — 스캔타임 고려 |
| 디바이스 주소 매핑 | D/M/X/Y 등 종류와 워드/비트 단위 정확히 구분 |
| PLC 파라미터 설정 | 이더넷/오픈 설정 미스매치로 연결 실패하는 경우가 많음 |
| 테스트 환경 | 실제 라인 적용 전 시뮬레이터/예비 PLC로 검증 권장 |

---

## 8. 전체 통합 아키텍처

```
GX Works2 이더넷/오픈 설정
   ↓
pymcprotocol로 연결 (plc_comm.py)
   ↓
equipment.py 클래스로 설비 상태 판단
   ↓
logger.py로 CSV 누적 저장
   ↓
Pandas/Matplotlib 분석 → Scikit-learn 예지보전
```

### 통합 예시 코드 (main.py)

```python
from equipment import 설비
from plc_comm import PLC연결
from logger import 로그_저장
import time

plc = PLC연결('192.168.1.10', 5000)
plc.연결()

설비목록 = {'M01': 설비('M01', 정상사이클타임=5.0)}

try:
    for _ in range(20):
        for 설비ID, 설비객체 in 설비목록.items():
            사이클타임 = plc.사이클타임_읽기('D100')
            설비객체.사이클_기록(사이클타임)

            if 설비객체.이상여부(사이클타임):
                print(f"⚠ {설비ID} 이상 감지: {사이클타임}s")
                plc.경보_출력('M10')
                로그_저장('alarm_log.csv', 설비ID, '이상')
            else:
                로그_저장('normal_log.csv', 설비ID, '정상')
        time.sleep(1)
except KeyboardInterrupt:
    print("모니터링 종료")
finally:
    plc.연결종료()
```

---

## 9. 역할 분담 요약

| 영역 | PLC | 파이썬 |
|---|---|---|
| 강점 | 빠른 스캔타임, 안전 로직, 하드웨어 직접 제어 | 대용량 데이터 처리, 통계/AI 분석, 시각화 |
| 시간 단위 | ms 단위 실시간 | 초~일 단위 배치/분석 |
| 역할 | 지금 이 신호를 어떻게 처리할까 | 누적된 데이터로 무엇을 알 수 있을까 |

**개념 대응표**
- 함수 → PLC 서브루틴
- 클래스 → PLC 함수블록(FB)
- 모듈/패키지 → PLC 프로그램 블록 구성

## 10. 다음 학습 우선순위

1. 파이썬 기초 문법 + 함수/클래스/모듈 구조 (GX Works2 STL/FB 사고방식과 연결됨)
2. Pandas + Matplotlib/Seaborn으로 로그 데이터 분석 실습
3. pymcprotocol로 실제 PLC 통신 실습
4. Scikit-learn 기반 예지보전 모델 → 포트폴리오 구성
5. 추가 학습 후보: 시계열 데이터(datetime 인덱싱) 센서 로그 분석, GitHub 포트폴리오 정리
