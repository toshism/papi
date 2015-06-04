import requests

from flask.ext.cache import Cache

# TODO move this base service class to services?
# or somewhere more appropriate probably

class BaseService(object):
    def __init__(self, data, cache):
        self.data = data
        self.requests = requests
        # TODO figure out config structure for cache settings
        # TODO support manual cache key/callable
        # TODO support unless callable
        # see https://github.com/thadeusb/flask-cache/blob/1c60076b6d4c2df0ac1de54c59e63b4f780cecbc/flask_cache/__init__.py#L226
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
