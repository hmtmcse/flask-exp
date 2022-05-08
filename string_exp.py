import re

string_value = "alphan-umeric@123__ asd abc"
s = re.sub(r'[^a-zA-Z0-9\-]', '', string_value)
print(s)

identifier = "touhid@"
print(identifier.find("@"))
