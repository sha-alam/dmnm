def f(x):
    return x * x * x - 2 * x - 5


def falsi(a, b):
    if f(a) * f(b) >= 0:
        print("a and b is not vailed")
        return
    for i in range(100000):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"The root is {round(c, 4)}")


a = -2
b = 3
falsi(a, b)