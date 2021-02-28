import openpyxl

wb = openpyxl.load_workbook('sample_data.xlsx')
sheet = wb['Sheet1']

for row in range(1, sheet.max_row + 1):
    for column in range(sheet.max_column):
        print(sheet[row][column].value)

# print(sheet[1][0])