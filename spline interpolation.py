import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 0, 1, 0])

# Create a cubic spline interpolation function
cs = CubicSpline(x, y)

# Generate a dense range of x values for smooth plotting
x_dense = np.linspace(0, 4, 100)
y_dense = cs(x_dense)

# Plot data points and the spline
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_dense, y_dense, color='red', label='Cubic Spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.grid(True)
plt.show()
