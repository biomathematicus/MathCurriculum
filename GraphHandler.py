import CurriculumGraph

cg = CurriculumGraph.CurriculumGraph

#DEMO OF WORKING

# from GenEdgesCSV import GenEdgesCSV

cg.GenEdgesCSV(r'Frequency_List_Of_Topics.xlsx', "edges.csv")


#graph = nx.read_edgelist('edges.csv', delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
#nx.draw(graph, arrows=1, with_labels=1)

#genAdj = nx.adjacency_matrix(graph).todense()
#np.savetxt("adjacency.csv", genAdj, delimiter = ',')
#adjacency = np.genfromtxt("adjacency.csv", delimiter = ',')

#print(nx.shortest_path_length(graph, str(3), str(18)))

#np.savetxt("FW.csv", FloydWarshall(adjacency), delimiter = ',')