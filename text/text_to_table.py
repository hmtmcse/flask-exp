from terminaltables import AsciiTable, SingleTable, DoubleTable

table_data = [
    ['Heading1', 'Heading2', 'Heading3', 'Heading4'],
    ['row1 column1 uuuuuuuuuuuuuuuuuuu', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = AsciiTable(table_data)
print(table.table)

TABLE_DATA = (
    ('Platform', 'Years', 'Notes'),
    ('Mk5', '2007-2009', 'The Golf Mk5 Variant was\nintroduced in 2007.'),
    ('MKVI', '2009-2013', 'Might actually be Mk5.'),
)

title = 'Jetta SportWagen'

# AsciiTable.
table_instance = AsciiTable(TABLE_DATA, title)
table_instance.justify_columns[2] = 'right'
print(table_instance.table)
print()

# SingleTable.
table_instance = SingleTable(TABLE_DATA, title)
table_instance.justify_columns[2] = 'right'
print(table_instance.table)
print()

# DoubleTable.
table_instance = DoubleTable(TABLE_DATA)
table_instance.justify_columns[2] = 'right'
print(table_instance.table)

