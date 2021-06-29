import numpy as np
import pandas as pd
import networkx as nx
from numpy import genfromtxt

def GetSheet(excel_file, sheet_name): #GETS THE SPECIFIC SHEET WE WANT
        return pd.read_excel(excel_file, sheet_name)
        
def GetSheetNames(excel_file): #GENERATES THE SHEET NAMES
    return pd.ExcelFile(excel_file).sheet_names

def GetSheetList(excel_file): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
    EdgesList = []
    excelfiledata = pd.ExcelFile(excel_file)
    for i in range(0,len(GetSheetNames(excel_file))):
        if excelfiledata.sheet_names[i].startswith("Edges"):
            EdgesList.append(GetSheet(excel_file, excelfiledata.sheet_names[i]))
    return(EdgesList)

def GetEdgesList(excel_file): #GENERATES THE CONCATENATED LIST OF EDGES
    EdgesList = GetSheetList(excel_file)
    return pd.concat(EdgesList)

def GenEdgesCSV(excel_file, output_csv): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
    return GetEdgesList(excel_file).to_csv(output_csv, index=False, header=False)

def FloydWarshall(adjacency):
    v = int(np.sqrt(int(adjacency.size)))
    inf = np.infty
    dist = np.full((v,v), inf)
    for a in range(v):
        for b in range(v):
            if adjacency[a][b] == 1:
                dist[a][b] = adjacency[a][b]
        dist[a][a] = 0
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

#DEMO OF WORKING

# from GenEdgesCSV import GenEdgesCSV

GenEdgesCSV(r'Frequency_List_Of_Topics.xlsx', "edges.csv")


graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
#nx.draw(graph, arrows=1, with_labels=1)

genAdj = nx.adjacency_matrix(graph).todense()
np.savetxt("adjacency.csv", genAdj, delimiter = ',')
adjacency = np.genfromtxt("adjacency.csv", delimiter = ',')

#print(nx.shortest_path_length(graph, str(3), str(18)))

np.savetxt("FW.csv", FloydWarshall(adjacency), delimiter = ',')