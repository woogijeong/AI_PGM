import matplotlib.pylab as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

x= [[174],[152],[138],[128],[186]]
y= [71,55,46,38,88]

reg.fit(x,y)

print(reg.coef_)
print(reg.intercept_)
print(reg.score(x,y))

print(reg.predict([[178]]))