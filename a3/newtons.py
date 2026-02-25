import numpy as np

def f(x):
    x1, x2, x3 = x
    return np.array([
        x1**2 - 2*x1 + x2**2 - x3 + 1,
        x1*x2**2 - x1 - 3*x2 + x2*x3 + 2,
        x1*x3**3 - 3*x3 + x2*x3**2 + x1*x2
    ])

def jacobian_matrix(x):
    x1, x2, x3 = x
    return np.array([
        [2*x1 - 2, 2*x2, -1],
        [x2**2 - 1, 2*x1*x2 - 3 + x3, x2],
        [x3**3 + x2, x1, 3*x1*x3**2 - 3 + 2*x2*x3]
    ])

# Initial values
x = np.array([1.0, 2.0, 3.0])
errors = []

# We need a "true" root r to calculate e(k). 
# We'll run extra iterations to find a highly accurate r.
r_ref = x.copy()
for _ in range(50):
    r_ref = r_ref - np.linalg.solve(jacobian_matrix(r_ref), f(r_ref))

# Run the first 6 iterations and track errors
x_k = np.array([1.0, 2.0, 3.0])
for k in range(1, 7):
    x_next = x_k - np.linalg.solve(jacobian_matrix(x_k), f(x_k))
    error = np.linalg.norm(r_ref - x_next, 2)
    errors.append(error)
    x_k = x_next
    if k == 6:
        print(f"Iteration 6 Approximation: {x_k}")

ratio = errors[5] / errors[4] # e(6) / e(5)
print(f"Ratio e(6)/e(5): {ratio:.4f}")
