import pandas as pd
import numpy as np
import networkx as np
from numpy import genfromtxt
import GetSheet
import GetSheetNames
import GetSheetList
import GetEdgesList
import GenEdgesCSV
import FloydWarshall

class CurriculumGraph:
    
    
    adjacency = []
    labels = []
    minDistance = []
    
    def __init__(course):
        print("cow")