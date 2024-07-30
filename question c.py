import numpy as np

# Given data points
x_points = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_points = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Linear interpolation function
def linear_interpolation(x0, x1, y0, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# Define the points between which we are interpolating
x0, x1 = 2.00, 4.25
y0, y1 = 7.2, 7.1

# Interpolation for x = 4.0
x_interp = 4.0
y_interp = linear_interpolation(x0, x1, y0, y1, x_interp)

print(f"The value of y at x = {x_interp} is {y_interp:.2f}")
