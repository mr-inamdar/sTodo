from flask import Flask, render_template, request, redirect, url_for
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


load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

# Session security
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False

@app.route('/')
def renderPage():
    return render_template('index.html')

@app.route('/register')
def renderSinUpPage():
    return render_template('singup.html')

@app.route('/login')
def renderlogInPage():
    return render_template('login.html')

@app.route('/<int:id>', methods=['GET'])
@user_required
def homePage(id):
    if request.method == 'GET':
        responce = fetch_all_todos(id)

        if responce.success:
            return render_template('index.html', tasks=responce['allTodos'])

    

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

@app.route('/deleteTask/<int:todoId>', methods=['DELETE'])
@user_required
def deleteTask(todoId):
    if request.method == 'DELETE':
        return delete_todo(todo_id=todoId)


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

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))

    app.run(debug=True, port = port, use_reloader=False)