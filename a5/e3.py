import numpy as np

d = 5 # Polynomial degree

x = np.linspace(start=1, stop=5, num=12)

res = []
for i in range(12):
    sum = 0
    for k in range (d+1):
        sum += x[i]**k
    res.append(sum)

y = np.array(res)

print(y)

A = np.column_stack((np.ones(12), x**1, x**2, x**3, x**4, x**5))

print(A)

Q_hat, R_hat = np.linalg.qr(A, mode="reduced")

cond_nbr = np.linalg.cond(R_hat, p=2)

print(cond_nbr)
