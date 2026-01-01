import openpyxl

wb = openpyxl.Workbook()

sheetName = wb.active

sheetName['A1'] = 200
sheetName['A2'] = 300
sheetName['A3'] = '=SUM(A1:A2)'

sheetName.row_dimensions[1].height = 70

sheetName.column_dimensions['A'].width = 70

wb.save('formulaInExcel.xlsx')