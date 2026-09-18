from functools import wraps
from flask import session, jsonify


def user_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return jsonify({
                "success": False,
                "message": "Please login first"
            }), 401

        return func(*args, **kwargs)

    return wrapper