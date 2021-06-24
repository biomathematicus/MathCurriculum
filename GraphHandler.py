import numpy as np
#from csv import reader
import pandas as pd
import networkx as nx



def ExcelSpecificSheet(excel_file, sheet_name): #GETS THE SPECIFIC SHEET WE WANT
        return pd.read_excel(excel_file, sheet_name)
        
def EdgesSheetNames(excel_file): #GENERATES THE SHEET NAMES
    return pd.ExcelFile(excel_file).sheet_names

def EdgesSheetsList(excel_file): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
    EdgesList = []
    excelfiledata = pd.ExcelFile(excel_file)
    for i in range(0,len(EdgesSheetNames(excel_file))):
        if excelfiledata.sheet_names[i].startswith("Edges"):
            EdgesList.append(ExcelSpecificSheet(excel_file, excelfiledata.sheet_names[i]))
    return(EdgesList)

def EdgesConcatenator(excel_file): #GENERATES THE CONCATENATED LIST OF EDGES
    EdgesList = EdgesSheetsList(excel_file)
    return pd.concat(EdgesList)


#DEMO OF WORKING

EdgesConcatenator(r'FrequencyList3.xlsx').to_csv('edges.csv', index=False, header=False)

graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
nx.draw(graph, arrows=1, with_labels=1)

#nx.adjacency_matrix(graph).todense()

np.savetxt("Adjacency.csv", nx.adjacency_matrix(graph).todense(), delimiter = ",")

#nx.floyd_warshall_numpy(graph)

np.savetxt("LeastDistance.csv", nx.floyd_warshall_numpy(graph), delimiter = ",")