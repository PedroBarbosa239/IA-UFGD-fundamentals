import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


x =  np.array([0,25,50,75,100])
y = np.array([])

model = LinearRegression()
model.fit(x.reshape(-1,1),y)


print('a = ', model.intercept_)
print('b = ', model.coef_)

model.predict(np.array([[13],[14],[15],[16]]))

a = model.intercept_
b = model.coef_
plt.scatter(x,y,s=3)
plt.plot(x,(a+b*x),color='r')
plt.show