import os
from pprint import pprint

directory_tree = {}


def push_content(index, path_list, file_dir, tree):
    if path_list[index] in tree and index + 1 < len(path_list):
        tree[path_list[index]] = push_content(index + 1, path_list, file_dir, tree[path_list[index]])
    else:
        tree[path_list[index]] = file_dir
    return tree


for root, dirs, files in os.walk("listing"):
    file_dir_temp = {}
    for name in files:
        file_dir_temp[name] = "f"

    for name in dirs:
        file_dir_temp[name] = "d"

    path_list: list = root.split(os.sep)
    push_content(0, path_list, file_dir_temp, directory_tree)

pprint(directory_tree)
