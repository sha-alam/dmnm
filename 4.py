INF = 1000
def floyd_warshall(vertex, adjacency_matrix):
  
  for k in range(vertex):
    for i in range(vertex):
      for j in range(vertex):
        a_m[i][j] = min(a_m[i][j], a_m[i][k] + a_m[k][j])
  
  for i in range(vertex):
    for j in range(0,vertex):
      if a_m[i][j]==1000:
        print("INF",end='\t')
      else:
        print((a_m[i][j]),end='\t')
    print()

a_m = [
        [  0,   5, INF, 10],
        [  INF,   0, 3, INF],
        [  INF,   INF, 0,   1],
        [INF, INF, INF,   0]
      ]
floyd_warshall(4, a_m)
