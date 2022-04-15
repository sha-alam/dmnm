def func(x):
    return x * x * x - 2 * x - 5

def falsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
    for i in range(100000):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    print(f"The root is {round(c, 4)}")

    a = 2
    b = 3
    falsi(a, b)


