import numpy as np

# Define the function to integrate
def f(x):
    return np.sin(x)  # Example function: sine function

# Trapezoidal rule function
def trapezoidal_rule(a, b, n):
    """
    Estimate the integral of f(x) from a to b using the trapezoidal rule with n intervals.
    
    Parameters:
    a (float): Start of the interval
    b (float): End of the interval
    n (int): Number of intervals
    
    Returns:
    float: Approximate value of the integral
    """
    h = (b - a) / n  # Width of each interval
    x = np.linspace(a, b, n + 1)  # Generate n+1 equally spaced points from a to b
    y = f(x)  # Evaluate f(x) at each point
    
    # Trapezoidal rule formula
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    
    return integral

# Main function to test the trapezoidal rule
def main():
    a = 0  # Start of the interval
    b = np.pi  # End of the interval
    n = 10  # Number of intervals
    
    result = trapezoidal_rule(a, b, n)
    print(f"The approximate value of the integral is: {result:.6f}")

# Run the main function
if __name__ == "__main__":
    main()
