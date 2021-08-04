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
cg = CurriculumGraph(r'../Data/FrequencyListOfTopics.xlsx')

# print(cdb.LessonsClasses[0][1])
# for i in range(1,int(cdb.LessonsClasses.size/3)):
#     if int(cdb.LessonsClasses[i][1]) != int(cdb.LessonsClasses[i-1][1]):
#         print(int(cdb.LessonsClasses[i][1]))

# cdb.GenOpus()
# cdb.GenPagina()
# cdb.GenLinguaPagina()
# cdb.GenLinguaOpus()

# cdb.cursor.execute('DELETE FROM INTEREST')
# cdb.cursor.execute('DELETE FROM CATEGORY')
# cdb.cursor.execute('DELETE FROM LINGUA_PAGINA')
# cdb.cursor.execute('DELETE FROM LINGUA_OPUS')
# cdb.cursor.execute('DELETE FROM PAGINA')
# cdb.cursor.execute('DELETE FROM OPUS')

# cdb.cnxn.commit()

cdb.cursor.execute('SELECT * FROM LINGUA_PAGINA')
for row in cdb.cursor:
    print(row)

# print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

# for i in cdb.edgesnumbers:
#     print(i)

# print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

# for i in cg.SheetNameEdgesList:
#     print(i)

