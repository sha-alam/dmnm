x = [5, 6, 9, 11]
y = [12, 13, 14, 16]
value = 10
sum = 0
n = len(x)
for i in range(n): 
    p = 1
    for j in range(n):
        if i != j:
            p =p* (value - x[j]) / (x[i] - x[j])
    sum =sum+ p * y[i]
print(sum)
