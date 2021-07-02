from FunGetEdgesList import GetEdgesList

def GenEdgesCSV(excel_file, output_csv): #GENERATES THE .csv FILE OF EDGES FROM A .xslx
    return GetEdgesList(excel_file).to_csv(output_csv, index=False, header=False)