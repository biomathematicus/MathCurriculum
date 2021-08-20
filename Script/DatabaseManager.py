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

cdb.cursor.execute('DELETE FROM DOCTRINA WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM LINGUA_DOCTRINA')
cdb.cursor.execute('DELETE FROM LINGUA_PAGINA WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM LINGUA_OPUS WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM COLLAB_OPUS_XREF WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM INTEREST WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM Category WHERE Opus > 1000')
cdb.cursor.execute('DELETE FROM MATRIX WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM COMMUNICATIO WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM PAGINA WHERE id_opus > 1000')
cdb.cursor.execute('DELETE FROM OPUS WHERE id_opus > 1000')
cdb.cursor.commit()

cdb.GenOpus()
cdb.GenPagina()
cdb.GenLinguaPagina()
cdb.GenLinguaOpus()
cdb.GenMatrix()
cdb.GenDoctrina()
cdb.GenLinguaDoctrina()

# USE THIS TO VIEW THINGS.  REPLACE LINGUA_OPUS WITH WHATEVER TABLE YOU WANT.

# cdb.cursor.execute('SELECT * FROM LINGUA_OPUS')
# for row in cdb.cursor:
#     print(row)


# THESE TWO BELOW MAY NOT BE NEEDED EVER AGAIN IF THEY ARE NEEDED RUN THEM BOTH BEFORE RUNNING cdb.cursor.execute('DELETE FROM DOCTRINA WHERE id_opus > 1000')

#cdb.cursor.execute('create Table DOCTRINA (id_pagina int, id_opus int, id_doctrina int, dt_created datetime, dt_edited datetime,  id_created int, id_edited int)')

#cdb.cursor.execute('CREATE Table LINGUA_DOCTRINA (id_doctrina int, cd_lingua text, ds_doctrina text, dt_created datetime, dt_edited datetime,  id_created int, id_edited int)')