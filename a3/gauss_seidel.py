import numpy as np

# System setup
A = np.array([[15, -5, 1, 1.1],
              [0, 7, 2, -1],
              [2, -1, 9, -1],
              [1, 1.1, -1, -6]], dtype=float)
b = np.array([1, 1, 1, 1], dtype=float)
x = np.array([2, 1, 1, 1], dtype=float) # Initial value

# Gauss-Seidel 10 iterations
for _ in range(10):
    for i in range(len(b)):
        # Sum of A[i, j] * x[j] for all j except i
        sum_ax = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - sum_ax) / A[i, i]

# Calculate L2 Norm
l2_norm = np.linalg.norm(x)

print(f"Final vector x(10): {x}")
print(f"L2 Norm: {l2_norm:.4f}")
