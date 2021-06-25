#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:15:51 2021

@author: llywyllyn
"""

import numpy as np
import pandas as pd
import networkx as nx


from GetEdgesList import GetEdgesList

def GenEdgesCSV(excel_file, output_csv): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
    return GetEdgesList(excel_file).to_csv(output_csv, index=False, header=False)