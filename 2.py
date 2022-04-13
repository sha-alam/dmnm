import numpy as np
A = {1, 2, 3}
B = {1, 2}
output1 = [(a,b) for a in A for b in B if a>b]
print(output1)
outptu2 = np.array(output1).reshape(3,2)
print(outptu2)