import pathlib
from urllib.parse import urljoin
from urllib.request import pathname2url


# absolute_path_string = "application\client-proma"
#
# # out = pathlib.Path(absolute_path_string).as_uri()
# # print(out)
#
# out = pathname2url(absolute_path_string)
# print(out)


print(urljoin("//xyz", "///abcd/efgh/"))

url = "//"

is_absolute = False
if url.lower().startswith(("http://", "https://", "//")):
    is_absolute = True
print(is_absolute)
