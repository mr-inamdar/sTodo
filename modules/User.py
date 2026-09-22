from database import get_sql_connection
from werkzeug.security import generate_password_hash, check_password_hash

def find_by_email(email):
    try:
        db = get_sql_connection()
        cursor = db.cursor(dictionary=True)
        query = 'SELECT sName, sId, email, password FROM student WHERE email = %s'

        cursor.execute(query, (email,))
        user=cursor.fetchone()

        cursor.close()
        db.close()

        return user

    except Exception as e:
        print("DATABASE ERROR:", e)
        return None

def create_user(name, email, password):
    db = get_sql_connection()
    cursor = db.cursor()
    password_hash = generate_password_hash(password)

    query = 'INSERT INTO student(sName, email, password) Values(%s, %s, %s)'

    cursor.execute(query, (name, email, password_hash))

    db.commit()

    user_id = cursor.lastrowid

    cursor.close()
    db.close()

    return user_id

def verify_password(userPassword, password):
    return check_password_hash(
        userPassword,
        password
    )

def delete_user(email):
    db = get_sql_connection()
    cursor = db.cursor()

    query = 'DELETE FROM student WHERE email = %s'

    cursor.execute(query, (email,))

    db.commit()

    cursor.close()
    db.close()

    return

def find_by_id(id):
    db = get_sql_connection()
    cursor = db.cursor(dictionary=True)
    query = 'SELECT sName, sId, email FROM student WHERE sId = %s'

    cursor.execute(query, (id,))
    user=cursor.fetchone()

    cursor.close()
    db.close()

    return user
    