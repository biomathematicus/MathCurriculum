import networkx as nx
import numpy as np
from importlib import reload  
from sys import path
from os import getcwd
path.append(getcwd() + "\\..\\Class") 
from CurriculumGraph import CurriculumGraph

cg = CurriculumGraph(r'..\\Data\\FrequencyListOfTopics.xlsx','1073')
#nx.draw(cg.Graph, with_labels=True)
#print(nx.number_of_nodes(cg.Graph))
#print(cg.Route)
#print(cg.Edges)
#animal = Cow('Annie', 'Betsie')
#print(cg.CoursesEdgesList)
#p.say_hi()  

#person = Person
#a = cg('cow') #in parentheses put list of courses or stuff like that, but not yet. WIP

#DEMO OF WORKING

# cg.GenEdgesCSV(r'FrequencyListOfTopics.xlsx', "edges.csv")

#animal.moo('cow', 'pig')

#print(isinstance('Edges1053', str))
#print(pd.read_excel(r'FrequencyListOfTopics.xlsx', 'Edges1053'))

# graph = nx.read_weighted_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
# nx.draw(graph)
# graph = nx.DiGraph()
# graph.add_edge(1,2, weight = 11)
# graph.add_edge(2,1, weight = 11)
# graph.add_edge( 1, 3, weight = 30 )
# graph.add_edge(3,1,weight = 30 )
# graph.add_edge(2,4,weight = 12)
# graph.add_edge(4,2,weight = 12)
# graph.add_edge(2,5,weight = 2)
# graph.add_edge(5,2,weight = 2)
# graph.add_edge(3,4,weight = 19)
# graph.add_edge(4,3, weight = 19)
# graph.add_edge(3,6, weight = 4)
# graph.add_edge(6,3, weight = 4)
# graph.add_edge(4,5,weight = 11)
# graph.add_edge(5,4,weight = 11)
# graph.add_edge(4,6, weight = 9)
# graph.add_edge(6,4, weight = 9)
# graph.add_edge(7,5,weight = 1)
# graph.add_edge(7,6,weight = 1)
# graph.add_edge(7,4, weight = 20)
# nx.draw(graph, arrows=1, with_labels=1)





# adjacency = cg.GenAdjacency(graph)
#np.savetxt("adjacency.csv", cg.Adjacency, delimiter = ',')
#least_distance = cg.GenLeastDistance(cg.Adjacency)
#np.savetxt("least_distance.csv", cg.LeastDistance, delimiter = ',')
#route = cg.GenRoute(cg.Adjacency, cg.LeastDistance)
#np.savetxt("route.csv", cg.Route, delimiter = ',')
