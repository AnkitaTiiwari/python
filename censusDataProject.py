import openpyxl

wb = openpyxl.load_workbook(filename='censuspopdata.xlsx')

sheetname = wb['Population by Census Tract']

