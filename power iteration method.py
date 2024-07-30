import numpy as np

def power_iteration(A, num_simulations):
    b_k = np.random.rand(A.shape[1])  # Start with a random vector
    for _ in range(num_simulations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re normalize the vector
        b_k = b_k1 / b_k1_norm
    
    # The dominant eigenvalue can be estimated by calculating the Rayleigh quotient
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    return eigenvalue, b_k

# Example matrix
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Number of iterations
num_simulations = 1000

# Running Power Iteration Method
eigenvalue_pi, eigenvector_pi = power_iteration(A, num_simulations)
print("Power Iteration Method")
print("Eigenvalue:", eigenvalue_pi)
print("Eigenvector:", eigenvector_pi)
