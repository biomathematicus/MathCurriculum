import pandas as pd

from FunGetSheetList import GetSheetList


def GetEdgesList(excel_file): #GENERATES THE CONCATENATED LIST OF EDGES
    EdgesList = GetSheetList(excel_file)
    return pd.concat(EdgesList)