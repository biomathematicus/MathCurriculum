# import pandas as pd
# import numpy as np
# import networkx as np
# from numpy import genfromtxt
import FunGetSheet
import FunGetSheetNames
import FunGetSheetList
import FunGetEdgesList
import FunGenEdgesCSV
import FunFloydWarshall

class CurriculumGraph:
    
    def GenEdgesCSV(excel_file, output_csv):
        return FunGenEdgesCSV.GenEdgesCSV(excel_file, output_csv)
    
    def FloydWarshall(adjacency):
        return FunFloydWarshall.FloydWarshall(adjacency)
    
    def GetEdgesList(excel_file):
        return FunGetEdgesList.GetEdgesList(excel_file)
    
    def GetSheet(excel_file, sheet_name):
        return FunGetSheet.GetEdgesList(excel_file)
        
    def GetSheetList(excel_file):
        return FunGetSheetList.GetSheetList(excel_file)
    
    def FunGetSheetNames(excel_file):
        return FunGetSheetNames.GetSheetNames(excel_file)
    
    # adjacency = []
    # labels = []
    # minDistance = []
    
    # def __init__(course):
    #     print("cow")