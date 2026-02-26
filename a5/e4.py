import numpy as np

R = np.array([
    [-5,-7,-7.6, -19.6],
    [0, -1, -1.8, -2.8],
    [0, 0, 3, 3],
    [0, 0, 0, 0],
])

det_R = np.prod(np.diag(R))
print(det_R)
