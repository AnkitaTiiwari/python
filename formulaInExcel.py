import openpyxl

wb = openpyxl.workbook()

sheetName = wb.active

sheetName['A1'] = 200
sheetName['A2'] = 300
sheetName['A3'] = '=SUM(A1:A2)'

wb.save('formulaInExcel.xlsx')