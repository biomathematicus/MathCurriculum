# Add path to the Class folder. All classes can now be imported directly
from sys import path
from os import getcwd
import sys

from networkx.drawing.layout import planar_layout
path.append(getcwd() + "/../Class")
from CurriculumDB import CurriculumDB


# Load additional libraries
import networkx as nx
import numpy as np
import pandas as pd
import pyodbc

# NOTE TO USER: PLEASE ADD THE FOLLOWING LINE WITH THE APPROPRIATE PARAMETERS REPLACING THE ONES HERE
# cdb = CurriculumDB(excel_file, 'serverip', 'databasename', 'username', 'password')

cdb = CurriculumDB(r'../Data/FrequencyListOfTopics.xlsx', '127.0.0.1', 'ALICE_DEVELOPMENT', 'ALICE', 'edutronica')

# cdb.cursor.execute('DELETE FROM LINGUA_PAGINA')
# cdb.cursor.execute('DELETE FROM LINGUA_OPUS')
# cdb.cursor.execute('DELETE FROM PAGINA')
# cdb.cursor.execute('DELETE FROM OPUS')
# cdb.cnxn.commit()

# cdb.GenOpus()
# cdb.GenPagina()
# cdb.GenLinguaPagina()
# cdb.GenLinguaOpus()

# cdb.cursor.execute('SELECT * FROM PAGINA')
# for row in cdb.cursor:
#     print(row)