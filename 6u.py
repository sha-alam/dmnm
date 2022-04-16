import numpy as np

x = [1911, 1921, 1931, 1941, 1951, 1961]
y = [12, 15, 20, 27, 39, 52]
n = 1946
u = float((n - x[0]) / (x[1] - x[0]))
sum = y[0]
k = 1
coeff = u

for i in range(len(y) - 1):
    y = np.diff(y)
    sum += coeff * y[0]
    coeff = coeff * (u - k) / (k + 1)
    k += 1

print(sum)