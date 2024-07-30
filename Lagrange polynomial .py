import numpy as np

def lagrange_interpolation(x, y, xi):
    n = len(x)
    L = np.zeros(n)
    
    for i in range(n):
        L[i] = np.prod([(xi - x[j]) / (x[i] - x[j]) for j in range(n) if i != j])
    
    yi = np.sum([L[i] * y[i] for i in range(n)])
    return yi

# Given data points
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Compute the interpolation at a specific point xi
xi = 2.5
yi = lagrange_interpolation(x, y, xi)
print(f'Interpolated value at x={xi} is y={yi}')
