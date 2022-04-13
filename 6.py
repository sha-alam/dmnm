def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
n = 6
x = [1911, 1921, 1931, 1941, 1951, 1961]

y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 12
y[1][0] = 15
y[2][0] = 20
y[3][0] = 27
y[4][0] = 39
y[5][0] = 52

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print("")

value = 1946
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,"is", round(sum, 6))
