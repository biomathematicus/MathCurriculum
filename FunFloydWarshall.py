import numpy as np

def FloydWarshall(adjacency):
    v = int(np.sqrt(int(adjacency.size)))
    inf = np.infty
    dist = np.full((v,v), inf)
    for a in range(v):
        for b in range(v):
            if adjacency[a][b] == 1:
                dist[a][b] = adjacency[a][b]
        dist[a][a] = 0
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist