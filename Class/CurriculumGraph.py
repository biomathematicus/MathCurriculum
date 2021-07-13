import pandas as pd
import numpy as np
import networkx as nx

class CurriculumGraph:
    CoursesList = []
    SheetNameEdgesList = []
    excel_file = None
    EdgesSheetsList = []
    Edges = None
    Graph = None
    Aliases = None
    LabelDict = {}
    
    Adjacency = None
    LeastDistance = None
    Route = None
    
    def __init__(self, excel_file, *courses):
        for i in range(len(courses)):
            self.CoursesList.append(courses[i])   
        for i in range(len(self.CoursesList)):
            self.SheetNameEdgesList.append("Edges" + self.CoursesList[i])
        self.excel_file = excel_file
        if len(courses) == 0:
            self.CoursesList = pd.ExcelFile(excel_file).sheet_names
            self.SheetNameEdgesList = self.GetEdgesSheetNames()
        self.EdgesSheetsList = self.GetEdgesSheetsList()
        self.GetAliases()
        self.Edges = self.GetEdges()
        self.GenEdgesCSV()
        self.Graph = self.GenGraph()        
        self.GenLabelDict()
        self.Adjacency = self.GenAdjacency(self.Graph)
        self.LeastDistance = self.GenLeastDistance(self.Adjacency)
        self.Route = self.GenRoute(self.Adjacency, self.LeastDistance) 
        nx.draw(self.Graph, labels = self.LabelDict, with_labels = True)
        
    def GetEdgesSheetNames(self): #GENERATES THE SHEET NAMES (UGLY????)
        for i in range(len(self.CoursesList)):
            if self.CoursesList[i].startswith("Edges"):
                self.SheetNameEdgesList.append(self.CoursesList[i])
        return self.SheetNameEdgesList
    
    def GetAliases(self):
        self.Aliases = pd.read_excel(self.excel_file, sheet_name = 'Dict').to_numpy()
        return self.Aliases
    
    def GenLabelDict(self):
        for i in list(self.Graph):
            for j in range(len(self.Aliases[:,0])):
                if str(i) == str(self.Aliases[j,0]):
                    self.LabelDict[str(i)] = str(self.Aliases[j][1])
        return self.LabelDict

    def GetEdgesSheetsList(self): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
        EdgesSheetsList = []
        for i in range(len(self.SheetNameEdgesList)):
            EdgesSheetsList.append(pd.read_excel(self.excel_file, sheet_name = self.SheetNameEdgesList[i]))
        return EdgesSheetsList
    
    def GetEdges(self): #GENERATES THE CONCATENATED DATAFRAME (?) OF EDGES
        return pd.concat(self.EdgesSheetsList)
    
    def GenEdgesCSV(self): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
        return self.GetEdges().to_csv("edges.csv", index=False, header=False)
    
    def GenGraph(self):
        return nx.read_weighted_edgelist("edges.csv", delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
        
    
    def GetMatrix(self, input_filename):
        return np.genfromtxt(input_filename, delimiter = ',')
    
    def GenAdjacency(self,graph):
        inf = np.infty
        v = 0
        for i in graph.nodes:
            v = max(int(i),v)
        matrix = np.full((v+1,v+1), inf)
        for i in graph.nodes:
            for j in graph.nodes:
                if graph.has_edge(i,j):
                    matrix[int(i)][int(j)] = graph[i][j]['weight']
                elif i == j:
                    matrix[int(i)][int(j)] = 0
        return matrix
        
        
    def GenLeastDistance(self, adjacency):
        v = int(np.sqrt(int(adjacency.size)))
        inf = np.infty
        dist = np.full((v,v), inf)
        for a in range(v):
            for b in range(v):
                if (adjacency[a][b] != 0 and adjacency[a][b] != inf):
                    dist[a][b] = adjacency[a][b]
            dist[a][a] = 0
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
    
    def GenRoute(self, adjacency, least_distance):
        v = int(np.sqrt(int(adjacency.size)))
        inf = np.infty
        route = np.full((v,v),inf)
        for a in range(v):
            for b in range(v):
                if (adjacency[a][b] != 0 and adjacency[a][b] != inf):
                    route[a][b] = b
            route[a][a] = a
        for i in range(v):
            for j in range(v):
                if least_distance[i][j] == inf:
                    route[i][j] = i
                for k in range(v):
                    if (least_distance[i][j] >= least_distance[i][k] + least_distance[k][j] and adjacency[i][k] < inf and i != k and j != k and least_distance[i][j] != inf):
                        route[i][j] = k
        return route