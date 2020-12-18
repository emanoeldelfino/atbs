import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print('Workbook object holds the worksheets')
print("That's why we use indexing to acess a sheet inside it")
print(list(wb))

sheet = wb['Sheet1']

print('Sheet object holds its list of rows ')
print('which in its turn holds a tuple of cells from the row')
print('When we index in sheets we pass two indexes')
print('The number translates as indexing the sheet itself, to get a specific')
print('row, while the letter specifies a column')
print('Together they return a cell, otherwise a tuple of cell objects of')
print('Row/Column')
print(list(sheet))

