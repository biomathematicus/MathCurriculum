#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:14:35 2021

@author: llywyllyn
"""

import numpy as np
import pandas as pd
import networkx as nx


from GetSheet import GetSheet
from GetSheetNames import GetSheetNames

def GetSheetList(excel_file): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
    EdgesList = []
    excelfiledata = pd.ExcelFile(excel_file)
    for i in range(0,len(GetSheetNames(excel_file))):
        if excelfiledata.sheet_names[i].startswith("Edges"):
            EdgesList.append(GetSheet(excel_file, excelfiledata.sheet_names[i]))
    return(EdgesList)