import numpy as np

def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    
    return coef[0, :]

def newton_polynomial(x, y, xi):
    coef = divided_diff(x, y)
    n = len(x)
    yi = coef[0]
    
    for k in range(1, n):
        term = coef[k]
        for i in range(k):
            term *= (xi - x[i])
        yi += term
    
    return yi

# Given data points
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Compute the interpolation at a specific point xi
xi = 2.5
yi = newton_polynomial(x, y, xi)
print(f'Interpolated value at x={xi} is y={yi}')
