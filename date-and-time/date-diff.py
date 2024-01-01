from datetime import datetime

date_1 = '30/1/2020'
date_2 = '28/12/2020'

start = datetime.strptime(date_1, "%d/%m/%Y")
end = datetime.strptime(date_2, "%d/%m/%Y")

res = (end.year - start.year) * 12 + (end.month - start.month) + 1
print('Difference between dates in months:', res)

date_diff = [
    {"start": "1/1/2020", "end": "28/2/2020"}
]