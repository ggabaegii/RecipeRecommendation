import sqlite3
import json
import os



def insert_recipes_to_db(recipes):
    """
    JSON 데이터를 SQLite DB의 recipes 테이블에 삽입합니다.
    :param recipes: JSON 형식의 레시피 데이터
    """
    db_path = os.path.join(os.path.dirname(__file__), "C:/RecipeRecommendation/backend/app/database.db")

    # DB 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for recipe in recipes:
        try:
            # 레시피 데이터 준비
            recipe_name = recipe.get("recipe_name")
            category = recipe.get("category")
            description = recipe.get("description", "")
            ingredients = json.dumps(recipe.get("ingredients", []),ensure_ascii=False) # 리스트를 JSON 문자열로 저장
            substitutes = json.dumps(recipe.get("substitutes", {}),ensure_ascii=False)  # 딕셔너리를 JSON 문자열로 저장
            instructions = json.dumps(recipe.get("cooking_steps", []),ensure_ascii=False) # 리스트를 JSON 문자열로 저장
            cook_time = recipe.get("cooking_time", "")
            difficulty = recipe.get("difficulty", "보통").lower()
            image_url = recipe.get("image_url", "")

            print("name:", recipe_name)
            print("instruction:",instructions)
            print("ingredients",ingredients)
            print("substitutes:", substitutes)

            # INSERT 쿼리 실행
            cursor.execute("""
            INSERT OR IGNORE INTO recipes (
                recipe_name, category, description, 
                ingredients, substitutes, instructions, cook_time, 
                difficulty, image_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                recipe_name, category, description,
                ingredients, substitutes, instructions, cook_time,
                difficulty, image_url
            ))

        except sqlite3.Error as e:
            print(f"DB 삽입 오류: {e}")

    # 커밋 및 연결 종료
    conn.commit()
    conn.close()
    print("레시피 데이터 삽입 완료.")
