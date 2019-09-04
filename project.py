import xlrd

loc = ("/home/fireeater/csci/csci431/pythonprogram/project/projectData.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# sheet.cell_value(0,0)
# print(sheet.ncols)
sheet.cell_value(0, 0)


print(sheet.row_values(1))
