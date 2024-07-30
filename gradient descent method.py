import numpy as np

def f(x, y):
    return x**2 + y**2 - xy + x - y + 1

def gradient_f(x, y):
    df_dx = 2*x - y + 1  # Partial derivative with respect to x
    df_dy = 2*y - x - 1  # Partial derivative with respect to y
    return np.array([df_dx, df_dy])

def gradient_descent(lr=0.1, initial_guess=(0, 0), iterations=1000):
    x, y = initial_guess
    for _ in range(iterations):
        grad = gradient_f(x, y)
        x -= lr * grad[0]
        y -= lr * grad[1]
    return x, y

# Set parameters
learning_rate = 0.1
initial_guess = (0, 0)
iterations = 1000

# Perform Gradient Descent
x_min, y_min = gradient_descent(learning_rate, initial_guess, iterations)
print(f"Minimum found at x = {x_min}, y = {y_min}")
print(f"Minimum value of the function = {f(x_min, y_min)}")
