
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(y)

item_dict = {
    "a": {"order": 20},
    "b": {"order": 1},
    "c": {"order": 8},
    "d": {"order": 2},
}


print(item_dict.items())


def keyfunc(tup):
    key, d = tup
    return d["order"]


sorted_item_dict = sorted(item_dict.items(), key=keyfunc)
print(dict(sorted_item_dict))
