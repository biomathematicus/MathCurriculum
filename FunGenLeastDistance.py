import numpy as np
from FunFloydWarshall import FloydWarshall

def GenLeastDistance(adjacency, output_filename):
    return np.savetxt(output_filename, FloydWarshall(adjacency), delimiter = ',')

