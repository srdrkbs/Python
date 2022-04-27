"""
Floyd Warshall Algorithm: (shortest distance from all nodes)

"""
import math
def floydWarshall(graph,V):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    #print(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist




graph = [[0, 3, math.inf, 5],
         [2, 0, math.inf, 4],
         [math.inf, 1, 0,  math.inf],
         [math.inf, math.inf, 2, 0]]
print(floydWarshall(graph,4))
