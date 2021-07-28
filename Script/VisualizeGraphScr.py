# Add path to the Class folder. All classes can now be imported directly
from sys import path
from os import getcwd
path.append(getcwd() + "/../Class")
from CurriculumGraph import CurriculumGraph

# import plotting utils
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Load additional libraries
import networkx as nx
import numpy as np

# Instantiate the class and useful variables.
cg = CurriculumGraph(r'../Data/FrequencyListOfTopics.xlsx', '1073')
Adjacency = cg.Adjacency
LeastDistance = cg.LeastDistance
Route = cg.Route

# Show path from first to second argument
cg.PrintPath('0','3')

# Show graph
plt.show()