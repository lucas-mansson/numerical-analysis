import numpy as np

years = np.array([1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003])
productions = np.array([67052, 68008, 69803, 72024, 73400, 72063, 74669, 74487, 74065, 76777])

x = years - 1994

X = np.column_stack([np.ones(len(x)), x, x**2, x**3])

A = X.T @ X
b = X.T @ productions
beta = np.linalg.solve(A, b)

x_2026 = 2026 - 1994
y_2026 = beta[0] + beta[1]*x_2026 + beta[2]*x_2026**2 + beta[3]*x_2026**3

print(round(y_2026))
