import numpy as np
import matplotlib.pyplot as plt
# import scikit-learn as sklearn
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1000,2000,3000,4000,5000 ])

# matplot plotting the data points

# plt.plot(x, y)
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.title('Experience vs Salary')
# plt.show()

model = LinearRegression()
model.fit(x,y)

result = model.predict([[6]])

print(result)




