from itertools import product
import numpy
A = {1, 2, 3}
B = {1, 2}
# output1 = [(a,b) for a in A for b in B if a>b]
output1 = [(a,b) for a,b in product(A,B) if a>b]
print(output1)
output2 = numpy.array(output1).reshape(3,2)
print(output2)