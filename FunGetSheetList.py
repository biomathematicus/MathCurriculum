import pandas as pd


from FunGetSheet import GetSheet
from FunGetSheetNames import GetSheetNames

def GetSheetList(excel_file): #GENERATES THE LIST WITH SHEETS OF EDGES AS ELEMENTS
    EdgesList = []
    excelfiledata = pd.ExcelFile(excel_file)
    for i in range(0,len(GetSheetNames(excel_file))):
        if excelfiledata.sheet_names[i].startswith("Edges"):
            EdgesList.append(GetSheet(excel_file, excelfiledata.sheet_names[i]))
    return(EdgesList)