import FunGetSheet
import FunGetSheetNames
import FunGetSheetList
import FunGetEdgesList
import FunGenEdgesCSV
import FunFloydWarshall
import FunGenAdjacencyCSV
import FunGetAdjacency
import FunGenLeastDistance

class CurriculumGraph:
    
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
    
    def FunGetSheetNames(excel_file):
        return FunGetSheetNames.GetSheetNames(excel_file)
    
    def GenAdjacencyCSV(graph, output_filename):
        return FunGenAdjacencyCSV.GenAdjacencyCSV(graph, output_filename)
    
    def GetAdjacency(input_filename):
        return FunGetAdjacency.GetAdjacency(input_filename)
    
    def GenLeastDistance(adjacency, output_filename):
        return FunGenLeastDistance.GenLeastDistance(adjacency, output_filename)
    
    # adjacency = []
    # labels = []
    # minDistance = []
    
    # def __init__(course):
    #     print("cow")