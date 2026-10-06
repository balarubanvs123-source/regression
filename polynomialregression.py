import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1000, 1500, 2500, 5000, 8000])

# plt.plot(x, y)
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.title('Experience vs Salary')
# plt.show()

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)

result = model.predict(poly.transform([[6]]))

print(result)