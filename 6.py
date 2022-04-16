def r_cal(r, n):
    coeff = r
    for i in range(1, n):
        coeff = coeff * (r - i)
    return coeff


def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = 6
x = [1911, 1921, 1931, 1941, 1951, 1961]
y = [[0 for i in range(6)] for j in range(6)]
y[0][0] = 12
y[1][0] = 15
y[2][0] = 20
y[3][0] = 27
y[4][0] = 39
y[5][0] = 52
# print(y[3])
# calculating forward difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# displaying forward difference table
for i in range(n):
    print(x[i], end='\t')
    for j in range(n - i):
        print(y[i][j], end='\t')
    print()

# calculate population
value = 1946
r = (value - x[0]) / (x[1] - x[0])
sum = y[0][0]
for i in range(1, n):
    sum += (r_cal(r, i) * y[0][i]) / fact(i)
print(sum)
