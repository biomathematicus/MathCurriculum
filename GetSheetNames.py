#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:12:24 2021

@author: llywyllyn
"""

import numpy as np
import pandas as pd
import networkx as nx

        
def GetSheetNames(excel_file): #GENERATES THE SHEET NAMES
    return pd.ExcelFile(excel_file).sheet_names