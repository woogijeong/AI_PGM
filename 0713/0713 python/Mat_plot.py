import matplotlib.pyplot as plt
import numpy as np 


# x = [1,2,3]
# y = [1,2,3]
# plt.plot(x,y)
# plt.title("My Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# #plt.show()
# plt.savefig('picture.png')


# x = np.linspace(0, np.pi * 10, 500) # pi * 10 너비에, 500 개의 점 균일하게 찍기
# fig, axes = plt.subplots(2,1) #2개의 그래프가 들어가는 figure 생성
# axes[0].plot(x, np.sin(x)) # 첫 번째 그래프는 사인 그래프
# axes[1].plot(x, np.cos(x)) # 두 번째 그래프는 코사인 그래프
# fig.savefig("sin&cos.png")


# x = np.arange(-9 , 10)
# y = x ** 2 # 라인 스타일로는 - , : , -. , -- 등 사용 가능

# plt.plot(x, y, linestyle = ":", marker = "*")
# # x 축 및 y 축에서 특정 범위를 자를 수도 있습니다.

# plt.show()


# x = np.arange(-9, 10)
# y1 = x ** 2
# y2 = - x
# plt.plot(x, y1, linestyle = "-.", marker = "*", color = "red", label = "y = x * x")
# plt.plot(x, y2, linestyle = ":", marker = "o", color = "blue", label = "y = -x")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend(shadow = True, borderpad = 1) # 범례
# plt.show()


# x = np.arange(-9, 10)
# y1 = x ** 2
# plt.plot(x , y1, linestyle = ":", marker = "o", markersize = 8, markerfacecolor = "blue", markeredgecolor = "red")
# plt.show()


# 막대 그래프

# x = np.arange(-9, 10)
# plt.bar(x,x **2)
# plt.show()


# 누적 막대 그래프

# x = np.random.rand(10) #아래 막대
# y = np.random.rand(10) # 중간 막대
# z = np. random.rand(10) #위 막대
# data = [x, y, z]
# x_array = np.arange(10)
# for i in range(0,3): # 누적 막대의 종류가 3개
#     plt.bar(x_array, data[i], bottom=np.sum(data[:i],axis=0))

# plt.show()


# 스캐터 그래프

# x = np.random.rand(10)
# y = np.random.rand(10)
# colors = np.random.randint(0, 100, 10)
# sizes = np.pi * 1000 * np.random.rand(10)
# plt.scatter(x,y, c = colors, s= sizes, alpha = 0.7)
# plt.show()

