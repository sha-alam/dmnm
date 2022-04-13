INF = 1000000000
def floyd_warshall(vertex, adjacency_matrix):
  
  for k in range(0, vertex):
    for i in range(0, vertex):
      for j in range(0, vertex):
        adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
  print("o/d", end='')
  for i in range(0, vertex):
    print("\t{:d}".format(i+1), end='')
  print()

  for i in range(0, vertex):
    print("{:d}".format(i+1), end='')
    for j in range(0,vertex):
      print("\t{:d}".format(adjacency_matrix[i][j]), end='')
    print()

adjacency_matrix = [
          [  0,   5, INF, 10],
          [  INF,   0, 3, INF],
          [  INF,   INF, 0,   1],
          [INF, INF, INF,   0]
          ]
floyd_warshall(4, adjacency_matrix)
