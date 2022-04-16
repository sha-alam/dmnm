import numpy
m1 = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 0]
]
m2 = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

u_m=[[m1[i][j] or m2[i][j] for i in range(len(m1))] for j in range(len(m1[0]))]
i_m=[[m1[i][j] and m2[i][j] for i in range(len(m1))] for j in range(len(m1[0]))]

print(f'Matrix intersection: \n {numpy.array(i_m).reshape(3,3)}')
print(f'Matrix union: \n {numpy.array(u_m).reshape(3,3)}')
