from flask import Blueprint, jsonify, request
# from routes import *
# from routes import login_route, UPDATE_ROUTE, DELETE_USER_ROUTE
import routes
from routes2 import *
# from routes2 import Cons
import routes2


# Create a blueprint for user routes
users_bp = Blueprint('users', __name__, url_prefix=routes.login_route)
gitlab_blueprint = Blueprint("GitLab.com", __name__)
gitlab_server_blueprint = Blueprint("GitlabServer.com", __name__)


GRAPHQL_PREFIX = "/api/graphql"

# Route to simulate user login (GET method)
@users_bp.route('/')
def login():
    return jsonify({"message": "Login page"}), 200

# Route to simulate updating a user's login number (POST method)
@users_bp.route(routes.UPDATE_ROUTE, methods=['POST'])
def update_login():
    login_number = request.json.get("login_number")
    if not login_number:
        return jsonify({"error": "Missing login_number in request"}), 400
    return jsonify({"message": f"Login number updated to {login_number}"}), 200

# Route to simulate deleting a user (DELETE method)
@users_bp.route(routes.DELETE_USER_ROUTE, methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

@users_bp.route(Cons.DEFAULT_NAME, methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

@users_bp.route(Cons.SECOND_NAME, methods=['POST'])
def post_user():
    pass

@users_bp.route(routes2.Cons.THIRD_NAME, methods=['POST'])
def post_user():
    pass

@gitlab_blueprint.post(GRAPHQL_PREFIX)
@gitlab_server_blueprint.post(GRAPHQL_PREFIX)
def handle_graphql_request():
    pass
