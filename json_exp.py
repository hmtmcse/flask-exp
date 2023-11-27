import ast
import json

# some JSON:
x =  ""


try:
    json_sting = "[]"
    json_dict = json.loads(json_sting)
except:
    pass

data = ""


data_set = ["{'name': 'name', }"]
for data in data_set:
    json_dat = json.dumps(ast.literal_eval(data))
    dict_dat = json.loads(json_dat)
    print(dict_dat)
