import importlib
from flask import Flask, Response
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache(app)

app.config.from_object('settings')

app.config['DEBUG'] = True

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def index(path):
    endpoint = app.config['ENDPOINTS'].get(path)
    if not endpoint:
        # TODO log this or something
        # maybe just return a 404
        return "no endpoint"
    module_path = endpoint.get('service')
    if not module_path:
        # TODO log this or something
        return "no module"
    module_name, klass = module_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    service = getattr(module, klass)
    Service = service(endpoint['data'], cache)
    return Response(response=Service.get(),
                    status=200,
                    mimetype="application/json")


if __name__ == '__main__':
    app.run()
