# 파이썬 함수와 파일 입출력 정리

## 1. 함수 (Function)

반복되는 코드를 하나의 이름으로 묶어서 재사용하는 도구입니다.

### 1-1. 기본 구조

```python
def 함수이름(매개변수):
    # 실행할 코드
    return 결과값

# 사용
결과 = 함수이름(전달값)
```

```python
def 섭씨_화씨_변환(섭씨):
    화씨 = 섭씨 * 9/5 + 32
    return 화씨

print(섭씨_화씨_변환(25))  # 77.0
```

### 1-2. 매개변수 종류

**기본값 매개변수** — 값을 안 넣으면 기본값 사용
```python
def 압력_체크(압력, 기준값=100):
    if 압력 > 기준값:
        return "경고"
    return "정상"

print(압력_체크(105))       # 경고 (기준값 100 자동 적용)
print(압력_체크(105, 120))  # 정상 (기준값 직접 지정)
```

**여러 개 반환**
```python
def 통계_계산(데이터):
    return min(데이터), max(데이터), sum(데이터)/len(데이터)

최소, 최대, 평균 = 통계_계산([101, 99, 103, 98, 105])
```

**가변 인자 (`*args`, `**kwargs`)** — 개수가 정해지지 않은 인자 처리
```python
def 여러_센서_평균(*값들):
    return sum(값들) / len(값들)

print(여러_센서_평균(23.1, 24.5, 22.8, 25.0))
```

### 1-3. 람다 함수 (익명 함수)

한 줄짜리 간단한 함수. `sorted`, `map`, `filter`와 자주 함께 씁니다.

```python
# 일반 함수
def 제곱(x):
    return x ** 2

# 람다로 표현
제곱 = lambda x: x ** 2

# 실전 활용: 센서값 리스트를 오차 기준으로 정렬
로그 = [{'id': 'S1', '오차': 3.2}, {'id': 'S2', '오차': 1.1}]
정렬됨 = sorted(로그, key=lambda x: x['오차'])
```

### 1-4. 함수를 나눠야 하는 이유

- 같은 코드를 여러 번 안 써도 됨 (유지보수 쉬움)
- 기능 단위로 나누면 디버깅이 쉬움 — **PLC의 서브루틴/함수블록(FB)과 같은 사고방식**
- 테스트할 때 함수 하나씩 검증 가능

---

## 2. 파일 입출력 (File I/O)

### 2-1. 기본 방법 — `with` 구문 (필수 관용구)

`with`를 쓰면 파일을 자동으로 닫아줘서 안전합니다. (닫는 걸 깜빡해서 생기는 오류 방지)

```python
# 쓰기
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("설비 가동 시작\n")

# 읽기
with open('log.txt', 'r', encoding='utf-8') as f:
    내용 = f.read()
    print(내용)
```

### 2-2. 모드 정리

| 모드 | 의미 |
|---|---|
| `'r'` | 읽기 (기본값) |
| `'w'` | 쓰기 (기존 내용 덮어씀) |
| `'a'` | 이어쓰기 (기존 내용 뒤에 추가) |
| `'r+'` | 읽기+쓰기 |

### 2-3. 한 줄씩 읽기 (대용량 로그 파일에 유용)

```python
with open('sensor_log.txt', 'r', encoding='utf-8') as f:
    for 줄 in f:
        print(줄.strip())  # strip()으로 줄바꿈 문자 제거
```

### 2-4. CSV 파일 다루기

**csv 모듈 (기본)**
```python
import csv

# 쓰기
with open('production.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['시간', '설비ID', '불량여부'])
    writer.writerow(['09:00', 'M01', 0])

# 읽기
with open('production.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for 행 in reader:
        print(행)
```

**Pandas (실무에서는 이쪽을 훨씬 많이 씀)**
```python
import pandas as pd

df = pd.read_csv('production.csv')
df.to_csv('결과.csv', index=False)
```

### 2-5. 예외 처리와 함께 쓰기 (실무 필수)

파일이 없거나 형식이 이상해도 프로그램이 죽지 않게 방어합니다.

```python
try:
    with open('sensor_log.txt', 'r', encoding='utf-8') as f:
        데이터 = f.read()
except FileNotFoundError:
    print("로그 파일이 없습니다. 새로 생성합니다.")
    데이터 = ""
except Exception as e:
    print(f"알 수 없는 오류: {e}")
```

### 2-6. JSON 파일 (설정값, 구조화된 데이터 저장에 유용)

```python
import json

설정 = {'설비ID': 'M01', '기준압력': 100, '경고임계값': 120}

# 저장
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(설정, f, ensure_ascii=False, indent=2)

# 불러오기
with open('config.json', 'r', encoding='utf-8') as f:
    설정_불러옴 = json.load(f)
```

---

## 3. PLC 자동화와의 연계

지금 GX Works2로 하시는 작업과 파이썬 함수/파일 입출력이 실제로 만나는 지점입니다.

### 3-1. 데이터 흐름 개념도

```
PLC (X15, D레지스터 등) 
   ↓ (통신: MC프로토콜, OPC-UA, Modbus 등)
파이썬 스크립트 
   ↓ (함수로 가공)
CSV/JSON 파일 저장 
   ↓
Pandas로 분석 / 그래프 시각화
```

### 3-2. 실전 예시 — 사이클타임 로그 자동 저장

PLC에서 읽어온 값(여기선 예시로 임의 생성)을 함수로 처리하고 CSV에 누적 저장하는 구조입니다.

```python
import csv
import datetime

def 사이클_이상_체크(사이클타임, 기준값=5.0, 허용오차=0.5):
    """기준값 대비 오차가 크면 이상으로 판단"""
    if abs(사이클타임 - 기준값) > 허용오차:
        return True
    return False

def 로그_저장(파일명, 시간, 사이클타임, 이상여부):
    with open(파일명, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([시간, 사이클타임, '이상' if 이상여부 else '정상'])

# --- 실제 사용 (PLC 통신 라이브러리로 값을 받아왔다고 가정) ---
현재_사이클타임 = 5.8  # 실제로는 PLC에서 읽어온 D레지스터 값
현재_시간 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

이상여부 = 사이클_이상_체크(현재_사이클타임)
로그_저장('cycle_log.csv', 현재_시간, 현재_사이클타임, 이상여부)

if 이상여부:
    print("경고: 사이클타임 이상 감지 — 점검 필요")
```

### 3-3. 왜 이 조합이 중요한가

| PLC 쪽 역할 | 파이썬 쪽 역할 |
|---|---|
| 실시간 신호 처리, 안전 로직 (SET/RST 등) | 누적 데이터 저장, 통계 분석, 이상 탐지 |
| 빠른 스캔 타임 (ms 단위) | 대용량 로그 분석, 그래프/리포트 생성 |
| 현장 하드웨어 직접 제어 | AI/머신러닝으로 예지보전(predictive maintenance) 연결 |

즉, **PLC는 현장에서 정확하고 빠르게 동작**하고, **파이썬은 그 결과 데이터를 모아서 "왜 이런 문제가 생겼는지", "다음엔 언제 문제가 생길지"를 분석**하는 역할 분담입니다. 이게 스마트팩토리/자동화 훈련 과정에서 배우실 핵심 흐름이기도 합니다.

### 3-4. 실제 통신은 어떻게?

파이썬에서 미쓰비시 PLC와 직접 통신하려면 보통 아래 방법을 씁니다.
- **MC 프로토콜** 라이브러리 (예: `pymcprotocol`) — GX Works2 환경과 바로 연결 가능
- **OPC-UA** — 표준 산업 통신 프로토콜, 다양한 PLC 벤더 호환
- 간단하게는 PLC가 CSV/텍스트로 로그를 뽑아주면, 파이썬은 파일만 읽어서 분석 (통신 설정 없이 시작하기 좋은 방법)
