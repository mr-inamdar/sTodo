from database import get_sql_connection

def insertMyTodo(id, title, desc):
    db = get_sql_connection()
    cursor = db.cursor()

    query = 'INSERT INTO todos(title, description) VALUES(%s, %s) WHERE id = %s'

    cursor.execute(query, (title, desc, id))

    db.commit()

    cursor.close()
    db.close()

    return

def getMyTodos(id):
    db = get_sql_connection()
    cursor = db.cursor(dictionary=True)

    query = 'SELECT title, description, due_date, completed FROM todos WHERE id = %s'

    cursor.execute(query, (id,))
    todos =cursor.fetchall()

    cursor.close()
    db.close()

    return todos

def deleteMyTodo(id):
    db = get_sql_connection()
    cursor = db.cursor()

    query = 'DELETE FROM todos WHERE todoId = %s'

    cursor.execute(query, (id,))

    db.commit()

    cursor.close()
    db.close()

    return

def updateMyTodo(id, title, desc):
    db = get_sql_connection()
    cursor = db.cursor()

    if title:
        query = 'UPDATE todos SET title=%s WHERE todoId = %s'
        cursor.execute(query, (title, id))
    elif desc:
        query = 'UPDATE todos SET description=%s WHERE todoId = %s'
        cursor.execute(query, (desc, id))
    elif desc:
        query = 'UPDATE todos SET description=%s, title=%s WHERE todoId = %s'
        cursor.execute(query, (desc, title, id))

    db.commit()

    cursor.close()
    db.close()

    return
