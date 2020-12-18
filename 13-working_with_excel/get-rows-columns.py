import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

for cell_obj in sheet[sheet.max_row]:
	print(cell_obj.value)

print()

for cell_obj in sheet['B']:
	print(cell_obj.value)

