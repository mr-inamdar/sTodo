from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import os

from routes.authRoutes import (
    register,
    login,
    logout,
    delete_account
)

from routes.todoRoutes import fetch_all_todos, insert_todo, update_todo, delete_todo

from middleware.auth import user_required

load_dotenv(override=True)

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

# Session security
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False

@app.route('/')
def renderPage():

    user = None
    tasks = []

    if session.get("user_id"):
        user = {
            "sName": session.get("sName"),
            "email": session.get("email")
        }

        res = fetch_all_todos(session["user_id"])
        response = res[0].get_json()
        tasks = response.get("allTodos", [])

    return render_template(
        'index.html',
        user=user,
        tasks=tasks
    )

@app.route('/register')
def renderSinUpPage():
    return render_template('singup.html')

@app.route('/login')
def renderlogInPage():
    return render_template('login.html')

@app.route('/<int:id>', methods=['GET'])
@user_required
def homePage(id):

    res = fetch_all_todos(id)

    user = {
        "sName": session.get("sName"),
        "email": session.get("email")
    }

    response = res[0].get_json()

    print("USER FOR JINJA:", user)

    if user:
        return render_template(
            'index.html',
            user=user,
            tasks=response['allTodos']
        )
    

@app.route('/addTask/<int:uid>', methods=['POST'])
@user_required
def addTask(uid):
    if request.method == 'POST':
        return insert_todo(user_id=uid)

@app.route('/updateTask/<int:uid>/<int:todoId>', methods=['PUT'])
@user_required
def updateTask(uid, todoId):
    if request.method == 'PUT':
        return update_todo(user_id=uid, todo_id=todoId)

@app.route('/deleteTask/<int:uId>/<int:todoId>', methods=['DELETE'])
@user_required
def deleteTask(uId, todoId):
    if request.method == 'DELETE':
        return delete_todo(user_id=uId, todo_id=todoId)


@app.route('/auth/register', methods=['POST'])
def singup():
    if request.method == 'POST':
       return register()
        

@app.route('/auth/login', methods=['POST'])
def logIn():
    if request.method == 'POST':
        return login()
        

@app.route('/auth/logout', methods=['POST'])
@user_required
def logout_user():
    logout()
    return redirect(url_for('login'))

@app.route('/auth/deleteAccount', methods=['DELETE'])
@user_required
def delete_user():
    if request.method == 'DELETE':
        return delete_account()

@app.route('/auth/sessionStatus')
def session_status():
    if session.get('user_id'):
        return jsonify({
            "loggedIn": True
        })

    return jsonify({
        "loggedIn": False
    }), 401

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))

    app.run(debug=True, port = port, use_reloader=False)