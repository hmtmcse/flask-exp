import re

to = ""
text = "test data / mia vai abc_x -"
print(re.sub(r'[^\w\s/\-]', to, text))

print("xyz, ".strip(", "))
