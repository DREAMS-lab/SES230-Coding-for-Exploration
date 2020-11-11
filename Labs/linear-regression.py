import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = 30*np.random.random((20,1))
slope = 0.5
intercept = 1.0
noise_vec =  np.random.normal(size=x.shape)
y_without_noise = slope * x + intercept
y = y_without_noise + noise_vec


model = LinearRegression()
model.fit(x,y)
num_elem = 30
x_new = np.linspace(0,30,num_elem)
x_new = x_new.reshape((num_elem,1))
y_new = model.predict(x_new)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y = 0.5x+1')
plt.plot(x_new,y_new,'.')
plt.plot(x, y_without_noise, 'r.')
print(model.coef_)
print(model.intercept_)
plt.show()