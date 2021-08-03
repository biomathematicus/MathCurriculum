# Add path to the Class folder. All classes can now be imported directly
from sys import path
from os import getcwd

from networkx.drawing.layout import planar_layout
path.append(getcwd() + "/../Class")
from CurriculumGraph import CurriculumGraph
from CurriculumDB import CurriculumDB

# import plotting utils
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Load additional libraries
import networkx as nx
import numpy as np
import pandas as pd
import pyodbc

# NOTE TO USER: PLEASE ADD THE FOLLOWING LINE WITH THE APPROPRIATE PARAMETERS REPLACING THE ONES HERE
# cdb = CurriculumDB(excel_file, 'serverip', 'databasename', 'username', 'password')

cdb = CurriculumDB(r'../Data/FrequencyListOfTopics.xlsx', '127.0.0.1', 'ALICE_DEVELOPMENT', 'ALICE', 'edutronica')

#cdb.GenOpus()
#cdb.GenPagina()
#cdb.GenLinguaOpus()
#cdb.GenLinguaPagina()
