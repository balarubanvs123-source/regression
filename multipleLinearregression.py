import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([1000, 2000, 3000, 4000, 5000])


model = LinearRegression()
model.fit(x, y)
prediction = model.predict([[6, 7]])
print(prediction)



plt.scatter(prediction, y)
# plt.plot(x,y)
plt.xlabel('number of hours')
plt.ylabel('Salary')
plt.title('Hours vs Salary')
plt.show()
