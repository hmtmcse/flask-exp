from urllib.parse import urlparse, urlencode, parse_qsl



# parsed = urlparse(url)
# current_params = dict(parse_qsl(parsed.query))
# new_params = {'location': 'United States'}
# merged_params = urlencode({**current_params, **new_params})
# parsed = parsed._replace(query=merged_params)
#
# print(parsed.geturl())

xyz_url = 'https://www.linkedin.com/jobs/search?keywords=engineer'
xyz_url2 = 'https://www.linkedin.com/jobs/search?y=30'

class URLProcessor:

    def get_query_params(self, url):
        parsed = urlparse(url)
        params = dict(parse_qsl(parsed.query))
        return params

    def add_query_params(self, url, params: dict):
        if not params:
            return url
        current_params = self.get_query_params(url)
        merged_params = urlencode({**current_params, **params})
        parsed = urlparse(url)
        parsed = parsed._replace(query=merged_params)
        return parsed.geturl()


url_processor = URLProcessor()
print(url_processor.add_query_params(xyz_url2, {"x": 100, "y": 300}))
