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

# 파이썬 머신러닝 입문 가이드

## 1. 머신러닝이란?

규칙을 사람이 직접 코딩하는 대신, **데이터로부터 규칙(패턴)을 스스로 학습**하게 만드는 방법입니다.

> PLC로 비유하면: 기존 방식은 "X15가 켜지면 Y29를 켜라"는 규칙을 사람이 직접 래더로 짜는 것. 머신러닝은 "이런 입력값들일 때 결과가 이랬다"는 데이터를 잔뜩 보여주고, 컴퓨터가 스스로 "X15와 Y29 사이엔 이런 관계가 있구나"를 찾아내게 하는 것입니다.

## 2. 머신러닝의 3가지 큰 종류

| 종류 | 하는 일 | 예시 |
|---|---|---|
| **지도학습** (Supervised) | 정답(라벨)이 있는 데이터로 학습 | 불량품 예측, 가격 예측 |
| **비지도학습** (Unsupervised) | 정답 없이 데이터의 패턴/그룹 찾기 | 고객 그룹 나누기 |
| **강화학습** (Reinforcement) | 시행착오로 보상을 최대화하는 행동 학습 | 로봇 제어, 게임 AI |

취업 훈련 과정 및 실무에서는 **지도학습**부터 접하게 될 확률이 높으니 여기에 집중하겠습니다.

## 3. 지도학습의 두 갈래

### 회귀 (Regression) — 숫자를 예측
"내일 온도가 몇 도일까?", "이 설비 수명이 며칠 남았을까?"

### 분류 (Classification) — 카테고리를 예측
"이 제품은 양품일까 불량일까?", "이 신호는 정상일까 이상일까?"

## 4. 핵심 워크플로우 (모든 머신러닝의 공통 흐름)

```
데이터 준비 → 학습용/테스트용 분리 → 모델 학습 → 예측 → 성능 평가
```

이 5단계는 어떤 알고리즘을 쓰든 거의 항상 동일합니다.

## 5. 실습 예시 1 — 분류: 불량품 예측

가동시간, 온도로 불량 여부를 예측하는 간단한 모델입니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 준비 (실제로는 CSV에서 불러옴)
data = {
    '가동시간': [120, 95, 130, 80, 110, 140, 70, 125],
    '온도': [45, 38, 50, 33, 42, 55, 30, 48],
    '불량여부': [0, 1, 1, 0, 0, 1, 0, 1]  # 0=양품, 1=불량
}
df = pd.DataFrame(data)

X = df[['가동시간', '온도']]  # 입력 (특징, feature)
y = df['불량여부']            # 정답 (라벨, label)

# 2. 학습용/테스트용 분리 (80% 학습, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 학습 (의사결정나무 - 가장 직관적인 알고리즘)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. 예측
predictions = model.predict(X_test)

# 5. 성능 평가
print(f"정확도: {accuracy_score(y_test, predictions):.2f}")

# 새로운 데이터로 예측해보기
new_data = pd.DataFrame({'가동시간': [100], '온도': [40]})
result = model.predict(new_data)
print("예측 결과:", "불량" if result[0] == 1 else "양품")
```

## 6. 실습 예시 2 — 회귀: 수치 예측

가동시간으로 전력 소비량을 예측하는 예시입니다.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# 데이터
가동시간 = np.array([[80], [95], [110], [120], [140]])
전력소비 = np.array([15, 18, 21, 23, 27])

# 학습
model = LinearRegression()
model.fit(가동시간, 전력소비)

# 예측
예측값 = model.predict([[100]])
print(f"가동시간 100분일 때 예상 전력소비: {예측값[0]:.1f}")

# 기울기와 절편 확인 (1차 방정식 y = ax + b 형태)
print(f"기울기: {model.coef_[0]:.3f}, 절편: {model.intercept_:.3f}")
```

## 7. 꼭 알아야 할 핵심 용어

| 용어 | 의미 |
|---|---|
| **Feature (특징)** | 모델에 넣는 입력값들 (예: 가동시간, 온도) |
| **Label (라벨)** | 맞춰야 할 정답 (예: 불량여부) |
| **Train/Test Split** | 학습용 데이터와 실력 테스트용 데이터를 나누는 것 |
| **Overfitting (과적합)** | 학습 데이터만 너무 잘 맞추고 새 데이터엔 못 맞추는 현상 |
| **Accuracy (정확도)** | 얼마나 잘 맞췄는지 비율 |

## 8. 자주 쓰는 알고리즘 난이도 순

1. **선형/로지스틱 회귀** — 가장 기본, 직선으로 관계 표현
2. **의사결정나무 (Decision Tree)** — 조건문(if-else)의 연속처럼 직관적
3. **랜덤 포레스트 (Random Forest)** — 의사결정나무 여러 개를 조합 (정확도↑)
4. **K-최근접이웃 (KNN)** — "비슷한 애들끼리 묶는다"는 단순한 원리
5. **딥러닝 (신경망)** — 더 복잡한 패턴, IoT/이미지 데이터에 강함

## 9. 학습 순서 추천

1. Pandas/NumPy로 데이터 다루기에 익숙해지기 (선행 필수)
2. Scikit-learn으로 회귀 → 분류 순서로 실습
3. 정확도뿐 아니라 정밀도/재현율 등 평가지표 이해
4. 필요시 딥러닝(TensorFlow/PyTorch)으로 확장 — IoT 센서 데이터, 이미지 분석에 유용

훈련 과정에 AI/빅데이터가 포함되어 있으니, 이 정도 기초를 미리 익혀두면 실습 진도를 훨씬 편하게 따라가실 수 있을 겁니다. 혹시 특정 알고리즘(예: 랜덤포레스트, 딥러닝)을 더 깊게 다뤄볼까요?
