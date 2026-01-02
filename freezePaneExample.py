import openpyxl

wb = openpyxl.load_workbook('freezeExample.xlsx')

sheetName = wb.active
sheetName.freeze_panes = 'C3'

wb.save('freezeExample1.xlsx')