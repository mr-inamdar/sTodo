from flask import request, jsonify, session

from modules.User import (
    findByEmail,
    create_user,
    verify_password,
    deleteUserRecord
)

def singIn():
    try:
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        password = data.get('pass')

        if not(name and email and password):
            return jsonify({
                "success": False,
                "message": "Name, email and password are required"
            }), 400
        
        user = findByEmail(email)

        if user:
            return jsonify({
                "success": False,
                "message": "Email is alredy exits"
            }), 409

        user_id = create_user(name, email, password)

        return jsonify({
            "success": True,
            "message":"Account created successfully",
            "user_id": user_id
        }), 201
        

    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "message":e
        }), 404

def login():
    try:
        data = request.get_json()

        email = data.get('email')
        password = data.get('pass')

        if not(email and password):
           return jsonify({
                "success": False,
                "message": "Name, email and password are required"
            }), 400 

        user = findByEmail(email)

        if not user:
            return jsonify({
                "success": False,
                "message": "Email is not exits"
            }), 404

        if not verify_password(user["pass"], password):
            return jsonify({
                "success": False,
                "message": "Incorrect Password"
            }), 401

        session.clear()

        session["user_id"] = user["sId"]

        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": {
                user["pass"],
                user["sId"],
                user["sName"]
            }
        })
    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "message":e
        }), 404


def logout():
    session.clear()

    return jsonify({
        "success": True,
        "message": "Logout successful"
    }), 201

def deleteAccount():
    try:
        data = request.get_json()

        email = data.get('email')
        password = data.get('pass')

        if not(email and password):
            return jsonify({
                "success": False,
                "message": "Internal Error "
            }), 500

        user = findByEmail(email)
        
        if user:
            return jsonify({
                "success": False,
                "message": "Email is alredy exits"
            }), 409

        if not verify_password(user["pass"], password):
            return jsonify({
                "success": False,
                "message": "Incorrect Password"
            }), 401

        deleteUserRecord(email)
        
        session.clear()

        return jsonify({
            "success": True,
            "message": "Account Deleted successful"
        })

    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "message":e
        }), 404
        
        