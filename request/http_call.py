# pip install requests

import requests

ploads = {'things': 2, 'total': 25}
response = requests.get('https://xkcd.com/1906/', params=ploads)
print(response.status_code)
print(response.headers)
print(response.text)
