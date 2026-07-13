# 파이썬 데이터 분석 핵심 패키지 설명 및 활용 예시

## 1. NumPy — 수치 연산의 기반

배열(array) 연산을 빠르고 효율적으로 처리하는 라이브러리입니다. Pandas를 포함해 대부분의 데이터 분석 라이브러리가 내부적으로 NumPy를 기반으로 동작합니다.

**핵심 개념**: 벡터화 연산 (반복문 없이 배열 전체에 연산 적용)

```python
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])

# 벡터화 연산 - 반복문 없이 한 번에 처리
print(arr * 2)          # [2 4 6 8 10]
print(arr.mean())        # 평균: 3.0
print(arr.std())         # 표준편차

# PLC 센서 데이터 예시: 여러 사이클의 압력값
pressure = np.array([101.2, 102.5, 99.8, 103.1, 100.4])
print(f"평균 압력: {pressure.mean():.2f}")
print(f"최대 편차: {pressure.max() - pressure.min():.2f}")
```

## 2. Pandas — 데이터 분석의 핵심

표(DataFrame) 형태로 데이터를 다루는 라이브러리입니다. 엑셀을 코드로 다룬다고 생각하면 됩니다.

**핵심 개념**: DataFrame(표), Series(한 열)

```python
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('sensor_log.csv')

# 데이터 구조 파악
df.head()        # 상위 5행 확인
df.info()        # 컬럼 타입, 결측치 개수 확인
df.describe()    # 평균, 표준편차 등 통계 요약

# 실무 예시: 설비 가동 로그 분석
df = pd.DataFrame({
    '설비ID': ['M01', 'M02', 'M01', 'M03', 'M02'],
    '가동시간': [120, 95, 130, 80, 110],
    '불량여부': [0, 1, 0, 0, 1]
})

# 설비별 평균 가동시간, 불량률 집계
result = df.groupby('설비ID').agg(
    평균가동시간=('가동시간', 'mean'),
    불량건수=('불량여부', 'sum')
)
print(result)
```

**결측치 처리**
```python
df['가동시간'] = df['가동시간'].fillna(df['가동시간'].mean())  # 평균으로 채우기
df = df.dropna()  # 결측치 행 제거
```

## 3. Matplotlib — 기본 시각화

가장 널리 쓰이는 그래프 라이브러리입니다. 세밀한 커스터마이징이 가능합니다.

```python
import matplotlib.pyplot as plt

# 시간에 따른 온도 변화 그래프
time = [0, 1, 2, 3, 4, 5]
temp = [22.1, 22.5, 23.0, 23.8, 24.2, 24.5]

plt.plot(time, temp, marker='o')
plt.title('시간대별 온도 변화')
plt.xlabel('시간(h)')
plt.ylabel('온도(℃)')
plt.grid(True)
plt.show()
```

## 4. Seaborn — 통계 시각화 (Matplotlib 기반, 더 예쁘고 간결)

상관관계, 분포 등을 빠르게 시각화할 때 유용합니다.

```python
import seaborn as sns

# 여러 설비의 불량률 비교 - 막대그래프
sns.barplot(data=df, x='설비ID', y='불량여부')

# 변수 간 상관관계 히트맵
corr = df[['가동시간', '불량여부']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

## 5. Scikit-learn — 머신러닝 (기초 예측/분류)

데이터 분석에서 한 단계 더 나아가 예측 모델을 만들 때 사용합니다.

```python
from sklearn.linear_model import LinearRegression

# 가동시간으로 불량여부 예측하는 간단한 회귀 예시
X = df[['가동시간']]
y = df['불량여부']

model = LinearRegression()
model.fit(X, y)

print(model.predict([[100]]))  # 가동시간 100일 때 예측값
```

## 6. 기타 알아두면 좋은 패키지

| 패키지 | 용도 | 활용 예시 |
|---|---|---|
| `openpyxl` | 엑셀 파일 세부 제어 | 서식 유지한 채 엑셀 파일 수정 |
| `datetime` | 날짜/시간 처리 | 센서 로그의 타임스탬프 파싱 |
| `scipy` | 통계/과학 계산 | t-검정, 신호 처리(FFT 등) |
| `plotly` | 인터랙티브 시각화 | 웹 대시보드용 그래프 |

## 실전 조합 예시 — PLC 로그 분석 시나리오

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
df = pd.read_csv('plc_cycle_log.csv')

# 2. 데이터 정제
df['타임스탬프'] = pd.to_datetime(df['타임스탬프'])
df = df.dropna(subset=['사이클타임'])

# 3. 이상치 확인 (평균 ± 2표준편차 벗어난 사이클)
mean, std = df['사이클타임'].mean(), df['사이클타임'].std()
outliers = df[(df['사이클타임'] > mean + 2*std) | (df['사이클타임'] < mean - 2*std)]
print(f"이상 사이클 {len(outliers)}건 발견")

# 4. 시각화
plt.plot(df['타임스탬프'], df['사이클타임'])
plt.title('사이클타임 추이')
plt.show()
```

이 조합(Pandas + Matplotlib/Seaborn + NumPy)이 실무 데이터 분석의 90% 이상을 차지하니, 이 세 개를 먼저 확실히 다지고 여유되면 Scikit-learn으로 넘어가시는 걸 추천드립니다.
