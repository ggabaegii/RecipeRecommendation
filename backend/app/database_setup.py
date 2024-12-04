import sqlite3
import os

def create_recipes_table():
    """
    SQLite DB에 레시피 테이블 생성
    """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, 'database.db')
    if not os.path.exists(db_path):
        print("데이터베이스가 존재하지 않습니다. 새로 생성합니다.")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            description TEXT,
            ingredients TEXT NOT NULL,
            substitutes TEXT,
            instructions TEXT NOT NULL,
            cook_time TEXT,
            difficulty TEXT CHECK(difficulty IN ('쉬움', '보통', '어려움')) NOT NULL DEFAULT 'medium',
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        conn.close()
        print("데이터베이스 및 테이블이 성공적으로 생성되었습니다.")
    else:
        print("데이터베이스가 이미 존재합니다.")

def create_users_table():
    """
    SQLite DB에 사용자 테이블 생성
    """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        real_name TEXT NOT NULL,
        gender TEXT,
        birthdate TEXT,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        security_question_1 TEXT NOT NULL,
        security_answer_1 TEXT NOT NULL,
        security_question_2 TEXT NOT NULL,
        security_answer_2 TEXT NOT NULL,
        profile_picture BLOB
    )
    """)
    conn.commit()
    conn.close()
    print("사용자 테이블이 성공적으로 생성되었습니다.")
