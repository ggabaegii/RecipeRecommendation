import sqlite3

def create_recipes_table():
    """
    SQLite DB에 레시피 테이블 생성
    """
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        category TEXT,
        description TEXT,
        ingredients TEXT,
        substitutes TEXT,
        instructions TEXT,
        cooking_time TEXT,
        difficulty TEXT,
        image_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# 실행
if __name__ == "__main__":
    create_recipes_table()
    print("레시피 테이블 생성 완료.")
