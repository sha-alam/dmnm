from itertools import product
A={1,2,3,4}
print(f'A = {A}')
# R1=[(i,j) for i,j in product(A,A) if j%i==0]
R1=[]
for a,b in product(A,A):
    if a%b==0:
        R1+=[(a,b)]

R2=[(a,b) for a,b in product(A,A) if a<=b]
print(f'The pair list is for a/b: {R1}')
# print ("The pair list is for a/b : " + str(R1))
print (f'The pair list is for a<=b : {R2}')
