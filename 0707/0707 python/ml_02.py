
#################################

# 꽃 150 개 자료를 가지고 무슨 꽃인지 판별하기

import pandas as pd
from sklearn.datasets import load_iris
from sklearn import svm
import plotly.express as px

# iris = load_iris()
# # print(iris.data)

# # # print(iris.target)
# # # print(iris.target_names)
# # # print(iris.feature_names)
# # # print(iris.DESCR)

# # # df = pd.DataFrame(iris.data)
# # # print(df.head(5))  # 앞에서 5개만 추출


# df = pd.DataFrame(iris.data, columns=iris['feature_names'])


# # 결정경계가 얼마나 세밀하게 만들어질지 결정 (gamma)
# # 오분류를 얼마나 허용할지 결정 (C)
# # 값이 클수록 학습 데이터를 더 정확히 맞추려 함

# s = svm.SVC(gamma=0.1,C=10)   

# #모델 학습
# #입력(x):꽃의 특성 4가지
# #정답(y):꽃의 종류(0,1,2)


# s.fit(iris.data,iris.target)


# df.columns= ['꽃받침길이','꽃받침너비','꽃잎길이','꽃잎너비']

# new_d = [[6.4,3.2,6.0,2.5],[8.2,1.6,4.1,2.2]]
# res=s.predict(new_d)
# # print("새로운 2개 샘플의 부류는", iris.target_names[res])
# df = px.data.iris()

# fig = px.scatter_3d(
#     df,
#     x='sepal_length',
#     y='sepal_width',
#     z='petal_width',
#     color='species'
# )
# fig.show(renderer="browser")

from sklearn import datasets
import matplotlib.pyplot as plt
digit=datasets.load_digits()
plt.figure(figsize=(5,5))


# 0번 샘플을 그림
# plt.imshow(
#     digit.images[1500],
#     cmap=plt.cm.gray_r,
#     interpolation='nearest')


# plt.show()
for i in range(5):
    plt.figure(figsize=(2, 2))
    plt.imshow(digit.images[i], cmap=plt.cm.gray_r)
    plt.title(f"Label: {digit.target[i]}")
    plt.show()

print(digit.data[0])
# 0번 샘플의 화솟값을 출력
print("이 숫자는 ",digit.target[0],"입니다.")

"""
한 줄 요약
SVC: SVM을 이용한 분류(Classification) 모델
C: 오분류 허용 정도(규제 강도)
gamma: 각 데이터가 결정 경계에 미치는 영향 범위
kernel: 직선 또는 곡선 등 결정 경계의 형태를 결정하는 방식

"""