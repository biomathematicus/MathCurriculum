import numpy as np
import networkx as nx


def GenAdjacency(graph):
    matrix = nx.adjacency_matrix(graph).todense()
    inf = np.infty
    v =  int(np.sqrt(int(matrix.size)))
    for i in range(v):
        for j in range(v):
            if matrix[i,j] == 0 and i != j:
                matrix[i,j] = inf
    return matrix