import numpy as np

A = np.array([
        [4, 2, 3, 0], 
        [-2, 3, -1, 1], 
        [1, 3, -4, 2], 
        [1, 0, 1, -1], 
        [3, 1, 3, -2]
    ], dtype=int)

v1 = A[:, 0]
y1 = v1
q1 = y1 / np.linalg.norm(y1) 

print(q1)

v2 = A[:, 1]
y2 = v2 - q1 * (q1.transpose() @ v2)
q2 = y2 / np.linalg.norm(y2)

print(np.linalg.norm(y2))
print(q2)
