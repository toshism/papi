import importlib
from flask import Flask
app = Flask(__name__)

app.config.from_object('settings')

app.config['DEBUG'] = True

def index(*args, **kwargs):
    return kwargs['name']

for route, config in app.config['ENDPOINTS'].items():
    i = importlib.import_module(config['service'])
    app.add_url_rule(route, i.__name__, i.json, defaults=config['data'])


if __name__ == '__main__':
    app.run()
