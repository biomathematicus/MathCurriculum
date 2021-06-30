import CurriculumGraph
import networkx as nx
import numpy as np


cg = CurriculumGraph.CurriculumGraph #in parentheses put list of courses or stuff like that

#DEMO OF WORKING

#cg.GenEdgesCSV(r'Frequency_List_Of_Topics.xlsx', "edges.csv")


#graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
graph = nx.DiGraph()
graph.add_edge(1,2, weight = 11)
graph.add_edge(2,1, weight = 11)
graph.add_edge( 1, 3, weight = 30 )
graph.add_edge(3,1,weight = 30 )
graph.add_edge(2,4,weight = 12)
graph.add_edge(4,2,weight = 12)
graph.add_edge(2,5,weight = 2)
graph.add_edge(5,2,weight = 2)
graph.add_edge(3,4,weight = 19)
graph.add_edge(4,3, weight = 19)
graph.add_edge(3,6, weight = 4)
graph.add_edge(6,3, weight = 4)
graph.add_edge(4,5,weight = 11)
graph.add_edge(5,4,weight = 11)
graph.add_edge(4,6, weight = 9)
graph.add_edge(6,4, weight = 9)
graph.add_edge(7,5,weight = 1)
graph.add_edge(7,6,weight = 1)
graph.add_edge(7,4, weight = 20)
#nx.draw(graph, arrows=1, with_labels=1)

#cg.GenAdjacencyCSV(graph, "adjacency3.csv")
adjacency = cg.GetMatrix("adjacency2.csv")
cg.GenLeastDistance(adjacency, "FW2.csv")
least_distance = cg.GetMatrix("FW2.csv")
np.savetxt("Route2.csv", cg.GenRoute(adjacency, least_distance), delimiter = ',')
