def f(x):
    return x * x * x  - 2* x - 5

def bisection(a, b):
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b\n")
        return
    c = a
    for i in range(10000):
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f'The root is: {round(c,4)}')

a = 2
b = 3
bisection(a,b)
