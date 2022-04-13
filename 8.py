def proterm(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro

def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    return y

def applyFormula(value, x, y, n):
    sum = y[0][0]

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i])

    return sum

def printDiffTable(y, n):
    for i in range(n):
        print(x[i], end="\t\t")
        for j in range(n - i):
            print(y[i][j], end="\t\t")
        print("")

n = 6
y = [[0 for i in range(n)] for j in range(n)]
x = [4, 5, 7, 10, 11, 13]
print(x)
y[0][0] = 48
y[1][0] = 100
y[2][0] = 294
y[3][0] = 900
y[4][0] = 1210
y[5][0] = 2028
print(y)
y = dividedDiffTable(x, y, n)

printDiffTable(y, n)

value = 15
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 2))

value = 8
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 2))

