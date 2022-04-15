def func(x):
    return x * x * x  - 2* x - 5

def bisection(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return -1
    c = a
    for i in range(10000):
        c = (a + b) / 2
        if func(c) == 0.0:
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    print(f'The root is: {round(c,4)}')

a = 2
b = 3
bisection(a,b)
