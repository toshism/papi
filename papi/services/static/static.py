import json

from papi.lib.base_service import BaseService

class StaticData(BaseService):
    def fetch(self):
        return json.dumps(self.data)
