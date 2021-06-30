import numpy as np
from FunFloydWarshall import FloydWarshall
from FunGenAdjacencyCSV import GenAdjacencyCSV 

def RouteMatrix(adjacency, FloydWarshall, output_filename):
    v = int(np.sqrt(int(adjacency.size)))
    inf = np.infty
    route = np.full((v,v), inf)
    for i in range(v):
        for j in range(v):
            for k in range(v):
                if adjacency[i][j] >= adjacency[i][k]+adjacency[k][j] and FloydWarshall[i][k]<inf and i!=k and j!=k:
                    if adjacency[i][j] == inf:
                         route[i][j]=j
                    else :
                        route[i][j]=k
    return route
    return np.savetxt(output_filename, RouteMatrix(adjacency, FloydWarshall), delimiter = ',')
    print(RouteMatrix(adjacency, FloydWarshall, "Route.csv"))