from papi.lib.base_service import BaseService

class GitHub(BaseService):
    def base_url(self):
        return "https://api.github.com/users/%s" % self.data['username']

    def summary_url(self):
        return self.base_url() + "/events/public"

    def repos_url(self):
        return self.base_url() + "/repos"

    def fetch(self):
        data_type = self.data.get('data_type', 'summary')

        if data_type == 'summary':
            url = self.summary_url()
        elif data_type == 'repos':
            url = self.repos_url()

        return self.requests.get(url)
