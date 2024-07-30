import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1.2, 2.3, 2.8, 4.0, 4.1])

# Create a linear regression model and fit it
model = LinearRegression()
model = LinearRegression()
model.fit(x, y)

# Predict values
y_pred = model.predict(x)

# Plot data and regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred, color='red', label='Regression line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.grid(True)
plt.show()

print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_}")
