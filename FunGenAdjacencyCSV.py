import numpy as np
import networkx as nx

def GenAdjacencyCSV(graph, output_filename):
    return np.savetxt(output_filename, nx.adjacency_matrix(graph).todense(), delimiter = ',')

