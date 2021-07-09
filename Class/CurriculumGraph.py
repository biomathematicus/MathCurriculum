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

# A Sample class with init method  
class CurriculumGraph:
    CoursesList = []
    SheetNameEdgesList = []
    excel_file = None
    EdgesSheetsList = []
    Edges = None
    Graph = None
    
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
        self.Edges = self.GetEdges()
        self.GenEdgesCSV()
        self.Graph = self.GenGraph()
        self.Adjacency = self.GenAdjacency(self.Graph)
        self.LeastDistance = self.GenLeastDistance(self.Adjacency)
        self.Route = self.GenRoute(self.Adjacency, self.LeastDistance)
        
            
    # def GetEdgesSheet(self): #GETS THE SPECIFIC EDGES SHEET WE WANT
    #     for i in range(len(self.SheetNameEdgesList)):
    #         self.EdgesSheetsList.append(pd.read_excel(self.excel_file, sheet_name = self.SheetNameEdgesList[i]))
    #     return self.EdgesSheetsList
            
    def GetEdgesSheetNames(self): #GENERATES THE SHEET NAMES (UGLY????)
        for i in range(len(self.CoursesList)):
            if self.CoursesList[i].startswith("Edges"):
                self.SheetNameEdgesList.append(self.CoursesList[i])
        return self.SheetNameEdgesList

    def GetEdgesSheetsList(self): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
        #excelfiledata = pd.ExcelFile(self.excel_file)
        EdgesSheetsList = []
        for i in range(len(self.SheetNameEdgesList)):
            EdgesSheetsList.append(pd.read_excel(self.excel_file, sheet_name = self.SheetNameEdgesList[i]))
        return EdgesSheetsList
    
    def GetEdges(self): #GENERATES THE CONCATENATED DATAFRAME (?) OF EDGES
        # Edges = self.EdgesSheetsList[0]
        # for i in range(1, len(self.EdgesSheetsList)):
        #     Edges = pd.concat(Edges, self.EdgesSheetsList[i])
        # return Edges
        return pd.concat(self.EdgesSheetsList)
    
    def GenEdgesCSV(self): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
        return self.GetEdges().to_csv("edges.csv", index=False, header=False)
    
    def GenGraph(self):
        return nx.read_weighted_edgelist("edges.csv", delimiter=',', create_using=nx.DiGraph(), encoding="utf-8-sig")
        
    
    def GetMatrix(self, input_filename):
        return np.genfromtxt(input_filename, delimiter = ',')
    
    def GenAdjacency(self, graph):
        matrix = nx.adjacency_matrix(graph).todense()
        inf = np.infty
        v =  int(np.sqrt(int(matrix.size)))
        for i in range(v):
            for j in range(v):
                if matrix[i,j] == 0 and i != j:
                    matrix[i,j] = inf
        return matrix
    
    def GenLeastDistance(self, adjacency):
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
    
    def GenRoute(self, adjacency, least_distance):
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