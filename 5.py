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

union_matrix=[[m1[i][j] or m2[i][j] for i in range(len(m1))] for j in range(len(m1[0]))]
intersection_matrix=[[m1[i][j] and m2[i][j] for i in range(len(m1))] for j in range(len(m1[0]))]

print(f'Matrix intersection: {intersection_matrix}')
print(f'Matrix union: {union_matrix}')
