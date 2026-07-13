import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = sns.load_dataset('titanic')

#print(df.describe()) # 요약 통계

#print(df.describe(include='object')) # 문자열 컬럼의 통계

#print(df.count()) # 데이터 개수

#print(df.mean(numeric_only=True)) # 숫자값의 평균

#print(df['age'].mean()) # 나이의 평균

# condition = (df['adult_male']== True)
# print(df.loc[condition,'age'].mean())   #성인 남성의 평균

#print(df.mean(numeric_only=True, skipna=False)) #nan 값은 nan 으로 출력

#df2 = pd.Series([1,2,3,4,5]).median() #중앙값

#df2 = pd.Series([1,2,3,4,5,6]).median() # 짝수 개의 데이터인 경우 가운데 두 값의 평균

#print(f"나이 평균 : {df['age'].mean() :.5f}\n나이 중앙값 : {df['age'].median()}\n차이 : {df['age'].mean() - df['age'].median() : .5f}")

#print(df.loc[:,['age','fare']].sum()) # 열의 합

#print(df['age'].cumsum()) # 누적 합

#print(df['age'].cumprod()) # 누적 곱

# fare_mean = df['fare'].values.mean() # 평균

# my_var = ((df['fare'].values - fare_mean) ** 2).sum() / (df['fare'].count() - 1) # 분산
# print(my_var)

#print(df['fare'].var()) # 분산

#print(df['fare'].std()) # 표준편차

# print(df['age'].min()) #최소값

# print(df['age'].max()) #최대값

#print(df['age'].agg(['min','max','count','mean'])) # agg = 통합 통계 적용

#print(df[['age','fare']].agg(['min','max','count','mean'])) # 복수 컬럼에 대한 통합 통계 적용

#print(df['age'].quantile(0.1))  # 주어진 데이터를 동등한 크기로 분할 하는 지점

#print(df['who'].unique()) # 고유값

#print(df['who'].nunique()) # 고유값 개수

#print(df['who'].mode()) # 최빈값

#print(df['deck'].mode()) # 카테고리 가능

#print(df.corr(numeric_only=True)) # 상관관계 -1 ~ 1 , -1 에 가까울 수록 반비례, 1에 가까울 수록 정비례


