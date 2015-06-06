import importlib

from flask import Flask, Response, Blueprint, current_app
from flask.ext.cache import Cache

papi = Blueprint('papi', __name__)

# TODO move this into a file if nothing else ends up in papi dir

def get_class(path):
    module_name, klass = path.rsplit(".", 1)
    module = importlib.import_module(module_name)

    return getattr(module, klass)


@papi.route('/', defaults={'path': '/'})
@papi.route('/<path:path>')
def index(path):
    path = "/%s" % path
    endpoint = current_app.config['ENDPOINTS'].get(path)

    if not endpoint:
        # TODO figure out why this is ever happening
        # TODO log this or something
        # maybe just return a 404
        return "no endpoint"

    module_path = endpoint.get('service')
    if not module_path:
        # TODO log this or something
        return "no module"

    cache = Cache(current_app)

    service = get_class(module_path)
    Service = service(endpoint['data'], cache)
    result = Service.get()

    presenter_path = endpint.get('presenter')
    if presenter_path:
        presenter = get_class(presenter_path)
        Presenter = presenter(result)
        result = Presenter.transform()

    return Response(response=result,
                    status=200,
                    mimetype="application/json")
