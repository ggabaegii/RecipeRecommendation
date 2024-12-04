import sqlite3
import os

def insert_recipes_to_db(recipes):
    """
    JSON 데이터를 SQLite DB의 recipes 테이블에 삽입합니다.
    """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for recipe in recipes:
        try:
            recipe_name = recipe.get("recipe_name")
            category = recipe.get("category")
            description = recipe.get("description", "")
            ingredients = json.dumps(recipe.get("ingredients", []), ensure_ascii=False)
            substitutes = json.dumps(recipe.get("substitutes", {}), ensure_ascii=False)
            instructions = json.dumps(recipe.get("cooking_steps", []), ensure_ascii=False)
            cook_time = recipe.get("cooking_time", "")
            difficulty = recipe.get("difficulty", "보통").lower()
            image_url = recipe.get("image_url", "")

            cursor.execute("""
            INSERT OR IGNORE INTO recipes (
                recipe_name, category, description, ingredients, substitutes, instructions,
                cook_time, difficulty, image_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                recipe_name, category, description, ingredients, substitutes, instructions,
                cook_time, difficulty, image_url
            ))
        except sqlite3.Error as e:
            print(f"DB 삽입 오류: {e}")

    conn.commit()
    conn.close()
    print("레시피 데이터 삽입 완료.")

def insert_user_to_db(user_data):
    """
    사용자 데이터를 DB에 삽입
    """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (
            real_name, gender, birthdate, phone_number, email, 
            username, password, security_question_1, security_answer_1, 
            security_question_2, security_answer_2, profile_picture
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_data['real_name'],
            user_data.get('gender'),
            user_data['birthdate'],
            user_data['phone_number'],
            user_data['email'],
            user_data['username'],
            user_data['password'],
            user_data['security_question_1'],
            user_data['security_answer_1'],
            user_data['security_question_2'],
            user_data['security_answer_2'],
            user_data.get('profile_picture')
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"DB 삽입 오류: {e}")
    finally:
        conn.close()
