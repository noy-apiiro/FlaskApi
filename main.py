# main.py
from flask import Flask
from users import users_bp  # Import the blueprint for users

# Create the Flask application instance
app = Flask(__name__)

# Register the blueprint for user routes
app.register_blueprint(users_bp)

# Main route (just to verify the app is running)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
