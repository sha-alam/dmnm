from itertools import product
with open("one.txt", "r", encoding="utf-8") as g:
  	  S = list(map(int, g.readlines()))
print("S= "+str(S))
res1=[(i,j) for i,j in product(S,repeat=2) if i%j==0 or j%i==0]
res2=[(i,j) for i,j in product(S,repeat=2) if i<=j]
print ("The pair list is for a/b : " + str(res1))
print ("The pair list is for a<=b : " + str(res2))
