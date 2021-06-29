import pandas as pd
        
def GetSheetNames(excel_file): #GENERATES THE SHEET NAMES
    return pd.ExcelFile(excel_file).sheet_names