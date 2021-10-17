from flask import Blueprint
from flask import request
from flask import session
from flask import make_response

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        username = request.form["username"]
        password = request.form["password"]
        return make_response('authentication succeeded!', 200)
    except KeyError:
        return make_response('Invalid/Insufficent parameters', 401)
