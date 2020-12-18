import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(f'openpyxl workbook type {type(wb)}')

