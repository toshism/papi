import requests

from flask.ext.cache import Cache

class BaseService(object):
    def __init__(self, data, cache):
        self.data = data
        self.requests = requests
        self.cache_timeout = self.data.get('cache_timeout', 60*5)
        self.cache_key = self.__class__.__name__
        self.cache = cache

    def get(self):
        rv = self.cache.get(self.cache_key)
        if rv is None:
            rv = self.fetch()
            self.cache.set(self.cache_key, rv,
                           timeout=self.cache_timeout)
        return rv

    def fetch(self):
        raise NotImplemented("fetch method required")
