import numpy as np
import matplotlib as mp
import pandas as pd

# array1 = np.zeros((4,4), dtype=float)
# array2 = np.ones((4,4), dtype=float)
# array3 = np.random.randint(0, 10,(3,3))


# array4 = np.random.normal(0,1,(3,3))

# array = np.concatenate([array1, array2], axis=0)
# # print(array)

# # left, right = np.split(array,[2],axis=1)
# # # print(left)
# # # print(right)

# # print(np.sum(array,axis=1))

# data = {'Name':['Kim','park','Lee','Choi'],'Age':[20,23,21,26]}
# df = pd.DataFrame(data)
# print(df)


# array1 = pd.Series(np.arange(3,13,2),dtype='Float32')
# print(array1)

#arr = np.arange(100,105)

#s = pd.Series(arr)
# print(s)

# s = pd.Series(arr, dtype='int32')
# print(s)

# s = pd.Series(['부장', '차장','대리','사원','인턴'])
# print(s)

#s = pd.Series([91, 2.5, '스포츠', 4, 5.16])
#print(s)

# s = pd.Series(list('가나다라마'),dtype=object)
# print(s)


# sample = pd.Series(np.arange(10,51,10))
# sample.index = list('가나다라마')
# print(sample[['나','라']])


# np.random.seed(20)
# sample2 = pd.Series(np.random.randint(100,200,size=(15,)))


# # print(sample2[sample2<160])

# print(sample2[(130<=sample2) & (sample2<=170)])


# s = pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'], index=['가','나','다','라','마'], dtype=object)
# print(s)

# sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])

# print(sample[sample.isnull()])

# print(sample[sample.notna()])

# np.random.seed(0)
# sample = pd.Series(np.random.randint(100, 200, size=(10,)))


# print(sample[2:7])


# np.random.seed(0)
# sample2 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('가나다라마바사아자차'))

# print(sample2['바':'차'])

# print(sample2[:3])

# print(sample2['나':'바'])

####################################################

#DataFrame

# array = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['가','나','다'])
# print(array)

# data = {
#     'name':['kim','lee','park'],
#     'age': [24,27,34],
#     'children':[2,1,3]
# }

# # print(pd.DataFrame(data))

# df = pd.DataFrame(data)

# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.dtypes)
# print(df.T)

# df.index = list('abc')
# print(df)

# print(df['name'])
# print(type(df['name']))

# print(df[['name','children']])

# print(df.rename(columns={'name':'이름'}))

# print(df.rename(columns={'name':'이름'}, inplace=True))


# data = {'Food':['KFC','McDonald','SchoolFood'],'Price':[1000, 2000, 3000], 'Rating':[4.5, 3.9, 4.2]}
# df = pd.DataFrame(data)

# print(df)

# print(df[['Food','Rating']])

# print(df.rename(columns={'Food':'Place'}))