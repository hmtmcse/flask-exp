from typing import Pattern, Match
import re

mat = "typing.Dict[str, __main__.Address]"
mat1 = "typing.List[__main__.Degree]"

my_pattern = re.compile("typing\\.([A-Za-z]+)\\[([\w\\.,\s]+)]")  # type: Pattern[str]
my_match = re.match(my_pattern, mat)  # type: Match[str]
print(my_match)
print(my_match.group(1))
print(my_match.group(2))
