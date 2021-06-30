import FunGetSheet
import FunGetSheetNames
import FunGetSheetList
import FunGetEdgesList
import FunGenEdgesCSV
import FunFloydWarshall
import FunGenAdjacencyCSV
import FunGetMatrix
import FunGenLeastDistance
import FunGenRoute

class CurriculumGraph:
    
    # adjacency = []
    # labels = []
    # minDistance = []
    
    # CMR, MCA, MNI matrices put here
    
    # def __init__(course):
    #     print("cow")
    
    
    def GenEdgesCSV(excel_file, output_csv):
        return FunGenEdgesCSV.GenEdgesCSV(excel_file, output_csv)
    
    def FloydWarshall(adjacency):
        return FunFloydWarshall.FloydWarshall(adjacency)
    
    def GetEdgesList(excel_file):
        return FunGetEdgesList.GetEdgesList(excel_file)
    
    def GetSheet(excel_file, sheet_name):
        return FunGetSheet.GetEdgesList(excel_file)
        
    def GetSheetList(excel_file):
        return FunGetSheetList.GetSheetList(excel_file)
    
    def GetSheetNames(excel_file):
        return FunGetSheetNames.GetSheetNames(excel_file)
    
    def GenAdjacencyCSV(graph, output_filename):
        return FunGenAdjacencyCSV.GenAdjacencyCSV(graph, output_filename)
    
    def GetMatrix(input_filename):
        return FunGetMatrix.GetMatrix(input_filename)
    
    def GenLeastDistance(adjacency, output_filename):
        return FunGenLeastDistance.GenLeastDistance(adjacency, output_filename)
    
    def GenRoute(adjacency, least_distance):
        return FunGenRoute.GenRoute(adjacency, least_distance)
    
    