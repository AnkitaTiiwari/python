#would generate multiplication table up to n*n
import openpyxl

def create_multiplication_table(n):
    wb = openpyxl.Workbook()
    sheet = wb.active

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sheet.cell(row=i, column=j, value=i * j)

    wb.save('multiplication_table.xlsx')

number = int(input("Please enter Number : "))
create_multiplication_table(number)