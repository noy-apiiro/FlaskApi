# routes.py

BASE_API_ROUTE = "/api/private/v1"
login_route = f"{BASE_API_ROUTE}/login"
UPDATE_ROUTE = f"{login_route}/update"
DELETE_USER_ROUTE = f"{login_route}/delete/{{user_id}}"

class Cons:
    DEFAULT_NAME = "Sample"