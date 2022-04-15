INF = 1000
def floyd_warshall(vertex, adjacency_matrix):
  
  for k in range(vertex):
    for i in range(vertex):
      for j in range(vertex):
        adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
  
  for i in range(vertex):
    for j in range(0,vertex):
      # [print("INF\t") if adjacency_matrix[i][j]==1000 else print((adjacency_matrix[i][j]),end='\t')]
      print((adjacency_matrix[i][j]),end='\t')
    print()

adjacency_matrix = [
          [  0,   5, INF, 10],
          [  INF,   0, 3, INF],
          [  INF,   INF, 0,   1],
          [INF, INF, INF,   0]
          ]
floyd_warshall(4, adjacency_matrix)
