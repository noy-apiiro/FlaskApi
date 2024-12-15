# routes.py

BASE_API_ROUTE = "/api/private/v1"
LOGIN_ROUTE = f"{BASE_API_ROUTE}/login"
UPDATE_ROUTE = f"{LOGIN_ROUTE}/update"
DELETE_USER_ROUTE = f"{LOGIN_ROUTE}/delete/{{user_id}}"
