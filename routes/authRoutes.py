from flask import request, jsonify, session

from modules.User import (
    find_by_email,
    create_user,
    verify_password,
    delete_user
)

def register():
    print("REGISTER ROUTE HIT")

    data = request.get_json(silent=True)

    print("RECEIVED DATA:", data)

    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    print("NAME:", name)
    print("EMAIL:", email)
    print("PASSWORD RECEIVED:", bool(password))

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "Name, email and password are required"
        }), 400

    print("CHECKING EMAIL...")

    if find_by_email(email):
        return jsonify({
            "success": False,
            "message": "Email already exists"
        }), 409

    print("CREATING USER...")

    user_id = create_user(name, email, password)

    print("USER CREATED:", user_id)

    return jsonify({
        "success": True,
        "message": "Account created successfully",
        "user_id": user_id
    }), 201

def login():
    print('DEBUG raw request data:', request.get_data(as_text=True))
    data = request.get_json(force=True, silent=True)
    if not data:
        if request.form:
            data = request.form
        else:
            return jsonify({
                "success": False,
                "message": "Invalid JSON or form data"
            }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 400

    user = find_by_email(email)

    if not user:
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 401
    
    if not verify_password(user["password"], password):
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 401

    session.clear()
    session["user_id"] = user["sId"]
    session['sName'] = user['sName']
    session['email'] = user['email']
    
    return jsonify({
        "success": True,
        "message": "Login successful",
        "user": {
            "id": user["sId"],
            "name": user["sName"],
            "email": user["email"]
        }
    }), 200


def logout():

    session.clear()

    return jsonify({
        "success": True,
        "message": "Logout successful"
    }), 200


def delete_account():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON"
        }), 400

    password = data.get("password")

    if not password:
        return jsonify({
            "success": False,
            "message": "Password is required"
        }), 400

    from modules.User import find_by_id

    user = find_by_id(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404


    full_user = find_by_email(user["email"])

    if not verify_password(full_user["password"], password):
        return jsonify({
            "success": False,
            "message": "Incorrect password"
        }), 401

    delete_user(user["email"])

    session.clear()

    return jsonify({
        "success": True,
        "message": "Account deleted successfully"
    }), 200