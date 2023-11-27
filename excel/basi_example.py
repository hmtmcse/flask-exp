import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Car A', 'Car B', 'Car C', 'Car D', 'Car E'],
    'Price': [25000, 30000, 35000, 40000, 45000]
}

df = pd.DataFrame(data)

df.to_excel('output.xlsx', index=False)

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output-2.xlsx")
