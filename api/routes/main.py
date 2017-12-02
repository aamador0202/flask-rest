from api import api
from flask import Blueprint, make_response, request
from flask.views import MethodView

simple = Blueprint('simple', __name__)

import json

@simple.route('/')
@simple.route('/hello')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@simple.route('/test', methods = ['GET'])
def get_tasks():
    return make_response('Test successful!', 200)

class EchoRoute(MethodView):
    def get(self, id=None):
        if not id:
            return make_response('No id provided', 200)
        else:
            return make_response('The id is {}'.format(id), 200)
    def post(self):
        return make_response(request.json, 200)

echo_route =  EchoRoute.as_view('echo_route')
api.add_url_rule(
    '/echo', view_func=echo_route, methods=['GET', 'POST']
)
api.add_url_rule(
    '/echo/<int:id>', view_func=echo_route, methods=['GET']
)