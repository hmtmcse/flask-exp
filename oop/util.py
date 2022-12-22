class Util:
    urlPrefix: str = None

    def __init__(self, url_prefix: str = None):
        self.urlPrefix = url_prefix

    def get_url(self, url=None):
        prefix = "/"
        if self.urlPrefix:
            prefix = self.urlPrefix + "/"
        if url:
            return prefix + url
        return prefix
