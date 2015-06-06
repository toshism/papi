import importlib
from flask import Flask, Response

from papi import papi

app = Flask(__name__)

app.config.from_object('settings')

app.register_blueprint(papi, url_prefix='/papi')


@app.route('/')
def index():
    return "cool"


if __name__ == '__main__':
    app.run(debug=True)
