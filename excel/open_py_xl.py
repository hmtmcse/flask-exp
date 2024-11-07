from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

rows_count = (
    (14, 27),
    (22, 30),
    (42, 92),
    (51, 32),
    (16, 60),
    (63, 13)
)

for i in rows_count:
    sheet.append(i)

wb.save('formulas_book.xlsx')

# https://www.javatpoint.com/python-openpyxl
# https://realpython.com/openpyxl-excel-spreadsheets-python/
