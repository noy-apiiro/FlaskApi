# users.py
from flask import Blueprint, jsonify, request
from routes import LOGIN_ROUTE, UPDATE_ROUTE, DELETE_USER_ROUTE

# Create a blueprint for user routes
users_bp = Blueprint('users', __name__, url_prefix=LOGIN_ROUTE)

# Route to simulate user login (GET method)
@users_bp.route('/')
def login():
    return jsonify({"message": "Login page"}), 200

# Route to simulate updating a user's login number (POST method)
@users_bp.route('/update', methods=['POST'])
def update_login():
    login_number = request.json.get("login_number")
    if not login_number:
        return jsonify({"error": "Missing login_number in request"}), 400
    return jsonify({"message": f"Login number updated to {login_number}"}), 200

# Route to simulate deleting a user (DELETE method)
@users_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200
