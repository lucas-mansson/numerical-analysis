import numpy as np

def jacobi_method(A, b, x0, iterations):
    # Get the diagonal of A
    D = np.diag(A)
    # The rest of the matrix (L + U)
    R = A - np.diagflat(D)
    
    x = x0
    for _ in range(iterations):
        # Jacobi formula: x_new = (b - R*x) / D
        x = (b - np.dot(R, x)) / D
        
    return x

# 1. Define the system Ax = b
A = np.array([
    [3, 1, 1, 0],
    [1, 6, 3, -1],
    [6, 0, 9, -2],
    [1, 0, -1, -7]
], dtype=float)

b = np.array([10, 1, 1, 1], dtype=float)

# 2. Initial value x(0)
x0 = np.array([0, 1, 1, 0], dtype=float)

# 3. Perform 25 iterations
x_25 = jacobi_method(A, b, x0, 25)

# 4. Compute the L2 norm
l2_norm = np.linalg.norm(x_25)

# Display results
print(f"Vector x(25): {x_25}")
print(f"L2 Norm of x(25): {l2_norm:.4f}")
