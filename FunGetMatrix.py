import numpy as np
def GetMatrix(input_filename):
    return np.genfromtxt(input_filename, delimiter = ',')

    