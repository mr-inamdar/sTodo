import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_sql_connection():
    print("🔥 get_sql_connection START")

    host = os.getenv("HOST")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    database = os.getenv("DATABASE")

    print("HOST:", host)
    print("USER:", user)
    print("DATABASE:", database)
    print("PASSWORD EXISTS:", password is not None)

    try:
        print("🔥 BEFORE CONNECT")

        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        print("🔥 AFTER CONNECT")
        print("🔥 DATABASE CONNECTED")

        return db

    except Exception as e:
        print("❌ DATABASE ERROR:")
        print(type(e).__name__)
        print(str(e))

        raise