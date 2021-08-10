# Add path to the Class folder. All classes can now be imported directly
from sys import path
from os import getcwd
import sys

from networkx.drawing.layout import planar_layout
path.append(getcwd() + "/../Class")
from CurriculumDB import CurriculumDB
from CurriculumGraph import CurriculumGraph


# Load additional libraries
import networkx as nx
import numpy as np
import pandas as pd
import pyodbc

# NOTE TO USER: PLEASE ADD THE FOLLOWING LINE WITH THE APPROPRIATE PARAMETERS REPLACING THE ONES HERE
# cdb = CurriculumDB(excel_file, 'serverip', 'databasename', 'username', 'password')

cdb = CurriculumDB(r'../Data/FrequencyListOfTopics.xlsx', '127.0.0.1', 'ALICE_DEVELOPMENT', 'ALICE', 'edutronica')
# cdb.cursor.execute('DELETE FROM DOCTRINA')
#cdb.cursor.execute('DELETE FROM LINGUA_DOCTRINA')
# cdb.cursor.execute('DELETE FROM MATRIX')
# cdb.cursor.execute('DELETE FROM LINGUA_PAGINA')
# cdb.cursor.execute('DELETE FROM LINGUA_OPUS')
# cdb.cursor.execute('DELETE FROM PAGINA')
# cdb.cursor.execute('DELETE FROM OPUS WHERE id_opus > 1000')
#cdb.cnxn.commit()

#cdb.cursor.execute('DROP TABLE DOCTRINA')
#cdb.cnxn.commit()

# cdb.GenOpus()
# cdb.GenPagina()
# cdb.GenLinguaPagina()
# cdb.GenLinguaOpus()
#cdb.GenLinguaDoctrina()

# cdb.cursor.execute('SELECT * FROM DOCTRINA')
# for row in cdb.cursor:
#     print(row)

#cdb.GenMatrix()
#print(cdb.Adjacency[0][0])
#cdb.PaginaDict[1]
#print(int(np.sqrt(cdb.Adjacency.size)))

#cdb.cursor.execute('create Table DOCTRINA (id_pagina int, id_opus int, id_doctrina int, dt_created datetime, dt_edited datetime,  id_created int, id_edited int)')

#cdb.cursor.execute('CREATE Table LINGUA_DOCTRINA (id_doctrina int, cd_lingua text, ds_doctrina text, dt_created datetime, dt_edited datetime,  id_created int, id_edited int)')

#cdb.cursor.execute('DROP TABLE DOCTRINA')
#cdb.cursor.execute('DROP TABLE LINGUA_DOCTRINA')
#cdb.cursor.commit()
#cdb.GenDoctrina()