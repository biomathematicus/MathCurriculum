import CurriculumGraph
import networkx as nx
import numpy as np


cg = CurriculumGraph.CurriculumGraph

#DEMO OF WORKING

cg.GenEdgesCSV(r'Frequency_List_Of_Topics.xlsx', "edges.csv")


graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
nx.draw(graph, arrows=1, with_labels=1)

#cg.GenAdjacencyCSV(graph, "adjacency.csv")
#adjacency = cg.GetAdjacency("adjacency.csv")
#cg.GenLeastDistance(adjacency, "FW.csv")