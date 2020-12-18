import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active

print(list(sheet.columns)[1])

for cell_obj in list(sheet.columns)[1]:
	print(cell_obj.value)

print(list(sheet.rows)[-1])
for cell_obj in list(sheet.rows)[-1]:
	print(cell_obj.value)

