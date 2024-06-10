import re

pattern = re.compile("[a-z0-9_\\-]+")

validate = "aa"
response = pattern.fullmatch(validate)
print(response)


validate = "text-12processor"
pattern = re.compile(r"([a-z]+[a-z0-9_\\-]*)")
response = pattern.fullmatch(validate)
print(response)


target_string = "The price of PINEAPPLE ice cream is 20"
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)
print(result.groups())