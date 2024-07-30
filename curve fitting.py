import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function to fit
def model(x, a, b):
    return a * x**2 + b

# Generate some data
x_data = np.linspace(-0, 5, 25)
y_data = 2* x_data**2 + 1.0 + np.random.normal(size=x_data.size)

# Fit the model to the data
popt, pcov = curve_fit(model, x_data, y_data)

# Plot data and fit
plt.figure(figsize=(5, 5))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *popt), color='red', label='Fit')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.grid(True)
plt.show()
