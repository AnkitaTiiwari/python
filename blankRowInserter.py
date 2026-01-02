#insertes M blank rows after n rows in excel

import openpyxl

#will take input here
n= 2
m=3

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

for i in range(n+1):
    sheet.insert_rows(n+1) 

wb.save('produceSales_insertedBlanks.xlsx') 