#import FunGetSheet
#import FunGetSheetNames
#import FunGetSheetList
#import FunGetEdgesList
#import FunGenEdgesCSV
#import FunGetMatrix
#import FunGenLeastDistance
#import FunGenRoute
#import FunGenAdjacency
import pandas as pd
import numpy as np
import networkx as nx

class CurriculumGraph:
    
    def GetSheet(excel_file, sheet_name): #GETS THE SPECIFIC SHEET WE WANT
        if type(sheet_name) == str:
            sheets = pd.read_excel(excel_file, sheet_name)
        elif type(sheet_name) == list:
            sheets = []
            for i in range(0,len(sheet_name)):
                sheets.append(pd.read_excel(excel_file,sheet_name[i]))
        else:
            print("Please enter a list or a string as the second argument.  You probably forgot to enclose the name in apostrophes ")
        return sheets
            
    def GetSheetNames(excel_file): #GENERATES THE SHEET NAMES
        return pd.ExcelFile(excel_file).sheet_names

    def GetSheetList(excel_file): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
        EdgesList = []
        excelfiledata = pd.ExcelFile(excel_file)
        for i in range(0,len(CurriculumGraph.GetSheetNames(excel_file))):
            if excelfiledata.sheet_names[i].startswith("Edges"):
                EdgesList.append(CurriculumGraph.GetSheet(excel_file, excelfiledata.sheet_names[i]))
        return(EdgesList)
    
    def GetEdgesList(excel_file): #GENERATES THE CONCATENATED LIST OF EDGES
        EdgesList = CurriculumGraph.GetSheetList(excel_file)
        return pd.concat(EdgesList)
    
    def GenEdgesCSV(excel_file, output_csv): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
        return CurriculumGraph.GetEdgesList(excel_file).to_csv(output_csv, index=False, header=False)
    
    def GetMatrix(input_filename):
        return np.genfromtxt(input_filename, delimiter = ',')
    
    def GenAdjacency(graph):
        matrix = nx.adjacency_matrix(graph).todense()
        inf = 999999
        v =  int(np.sqrt(int(matrix.size)))
        for i in range(v):
            for j in range(v):
                if matrix[i,j] == 0 and i != j:
                    matrix[i,j] = inf
        return matrix
    
    def GenLeastDistance(adjacency):
        v = int(np.sqrt(int(adjacency.size)))
        inf = np.infty
        dist = np.full((v,v), inf)
        for a in range(v):
            for b in range(v):
                if adjacency[a,b] != 0:
                    dist[a][b] = adjacency[a,b]
            dist[a][a] = 0
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
    
    def GenRoute(adjacency, least_distance):
        v = int(np.sqrt(int(adjacency.size)))
        inf = 999999
        route = np.full((v,v),inf)
        for a in range(v):
            for b in range(v):
                if adjacency[a,b] == 1:
                    route[a][b] = a
            route[a][a] = a + 1
        for a in range(v):
            for b in range(v):
                route[a][b] = b + 1
        for i in range(v):
            for j in range(v):
                if least_distance[i][j] == inf:
                    route[i][j] = i + 1
                for k in range(v):
                    if (least_distance[i][j] >= least_distance[i][k] + least_distance[k][j] and adjacency[i,k] < inf and i != k and j != k and least_distance[i][j] != inf):
                        route[i][j] = k + 1
        return route
    
    # adjacency = []
    # labels = []
    # minDistance = []
    
    # CMR, MCA, MNI matrices put here
    
    # def __init__(course):
    #     print("cow")
    
    
    #def GenEdgesCSV(excel_file, output_csv):
    #    return FunGenEdgesCSV.GenEdgesCSV(excel_file, output_csv)
    
    #def GetEdgesList(excel_file):
    #    return FunGetEdgesList.GetEdgesList(excel_file)
    
    #def GetSheet(excel_file, sheet_name):
    #    return FunGetSheet.GetEdgesList(excel_file)
        
    #def GetSheetList(excel_file):
    #    return FunGetSheetList.GetSheetList(excel_file)
    
    #def GetSheetNames(excel_file):
    #    return FunGetSheetNames.GetSheetNames(excel_file)
    
   # def GenAdjacency(graph):
    #    return FunGenAdjacency.GenAdjacency(graph)
 
    #def GetMatrix(input_filename):
    #    return FunGetMatrix.GetMatrix(input_filename)
    
    #def GenLeastDistance(adjacency):
    #    return FunGenLeastDistance.GenLeastDistance(adjacency)
    
    #def GenRoute(adjacency, least_distance):
    #    return FunGenRoute.GenRoute(adjacency, least_distance)