#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:15:45 2021

@author: llywyllyn
"""

import numpy as np
import pandas as pd
import networkx as nx


from GetSheetList import GetSheetList


def GetEdgesList(excel_file): #GENERATES THE CONCATENATED LIST OF EDGES
    EdgesList = GetSheetList(excel_file)
    return pd.concat(EdgesList)