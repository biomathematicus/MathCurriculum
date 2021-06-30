import numpy as np

def GenRoute(adjacency, least_distance):
    v = int(np.sqrt(int(adjacency.size)))
    inf = np.infty
    route = np.full((v,v),inf)
    # for a in range(v):
    #     for b in range(v):
    #         if adjacency[a][b] == 1:
    #             route[a][b] = a
    #     route[a][a] = a + 1
    for a in range(v):
        for b in range(v):
            route[a][b] = b + 1
    for i in range(v):
        for j in range(v):
            for k in range(v):
                if (least_distance[i][j] >= least_distance[i][k] + least_distance[k][j] and adjacency[i,k] < inf and i != k and j != k):
                    if least_distance[i][j] == inf:
                        route[i][j] = j + 1
                    else:
                        route[i][j] = k + 1
    return route