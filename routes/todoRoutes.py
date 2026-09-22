from flask import jsonify, request

from modules.Todo import getMyTodos, updateMyTodo, deleteMyTodo, insertMyTodo
from modules.User import find_by_id

def insert_todo(user_id):

    data = request.get_json()
    
    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON"
        }), 400

    title = data.get('title')
    desc = data.get('desc')

    user = find_by_id(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User does not exist"
        }), 404

    insertMyTodo(id=user_id, title=title, desc=desc)

    return jsonify({
        "success": True,
        "message": "Todo added successfully"
    }), 200

def fetch_all_todos(user_id):

    user = find_by_id(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User does not exist"
        }), 404

    todos = getMyTodos(user_id)
    
    return jsonify({
        "success": True,
        "message": "Todos fetched successfully",
        "allTodos": todos
    }), 200


def update_todo(user_id, todo_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Invalid JSON"}), 400

    title = data.get("title")
    desc  = data.get("desc")

    if not (title or desc):
        return jsonify({"success": False, "message": "No fields to update"}), 400

    if not find_by_id(user_id):
        return jsonify({"success": False, "message": "User does not exist"}), 404

    if title and desc:
        todo = updateMyTodo(todo_id, title=title, desc=desc)
    elif title:
        todo = updateMyTodo(todo_id, title=title)
    else: 
        todo = updateMyTodo(todo_id, desc=desc)

    return jsonify({
        "success": True,
        "message": "Todo updated successfully",
        "Todo": todo
    }), 200


def delete_todo(user_id, todo_id):
    user = find_by_id(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User does not exist"
        }), 404
    
    deleteMyTodo(todo_id)

    return jsonify({
        "success": True,
        "message": "Todos fetched successfully"
    }), 200
