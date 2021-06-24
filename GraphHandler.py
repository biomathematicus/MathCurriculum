import numpy as np
#from csv import reader
import pandas as pd
import networkx as nx



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

def GenEdgesCSV(excel_file, output_csv): #GENERATES THE .csv file of edges from xlsx
    return GetEdgesList(excel_file).to_csv(output_csv, index=False, header=False)


#DEMO OF WORKING

#GenEdgesCSV(r'FrequencyListOfTopics.xlsx', "cow.csv")


#graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
#nx.draw(graph, arrows=1, with_labels=1)

#nx.adjacency_matrix(graph).todense()

#np.savetxt("Adjacency.csv", nx.adjacency_matrix(graph).todense(), delimiter = ",")

#nx.floyd_warshall_numpy(graph)

#np.savetxt("LeastDistance.csv", nx.floyd_warshall_numpy(graph), delimiter = ",")

#route = nx.all_pairs_shortest_path(graph)

#cow = nx.to_numpy_matrix(route)