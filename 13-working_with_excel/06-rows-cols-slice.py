import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'C3']))

for rows_obj in sheet['A1':'C3']:
	for cell_obj in rows_obj:
		print(cell_obj.coordinate, cell_obj.value)
	print('-- END OF ROW ---')

