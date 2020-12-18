import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(wb.sheetnames)

sheet = wb['Sheet3']

print(sheet)
print(type(sheet))

print(sheet.title)

another_sheet = wb.active

print(another_sheet)

