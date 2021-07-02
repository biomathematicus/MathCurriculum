import pandas as pd

def GetSheet(excel_file, sheet_name): #GETS THE SPECIFIC SHEET WE WANT
        return pd.read_excel(excel_file, sheet_name)
    