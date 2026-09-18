from flask import jsonify

from modules.Todo import (
    getMyTodos
)

from modules.User import (
    findById
)

def fetchAllTodos(id):
    try:
        if not id:
            return jsonify({
                "success": False,
                "message": "Internal Error"
            }), 400

        user = findById(id)

        if not user:
            return jsonify({
                "success": False,
                "message": "User dont exits"
            }), 400

        allTodos = getMyTodos(id=id)

        return jsonify({
            "success": True,
            "message":"Todos are fetched successfully",
            "allTodos": allTodos
        }), 201

    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "message":e
        }), 404