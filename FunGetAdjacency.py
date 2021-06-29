import numpy as np
def GetAdjacency(input_filename):
    return np.genfromtxt(input_filename, delimiter = ',')

    