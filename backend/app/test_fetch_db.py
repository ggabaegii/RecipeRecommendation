import sqlite3

def fetch_all_recipes():
    """
    SQLite DB에서 모든 레시피 데이터를 조회합니다.
    """
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect("C:/RecipeRecommendation/backend/app/database.db")
        cursor = conn.cursor()

        # 모든 레시피 조회
        cursor.execute("SELECT * FROM recipes")
        rows = cursor.fetchall()

        # 조회된 데이터 출력
        for row in rows:
            print(f"레시피 ID: {row[0]}")
            print(f"레시피 이름: {row[1]}")
            print(f"카테고리: {row[2]}")
            print(f"설명: {row[3]}")
            print(f"재료: {row[4]}")
            print(f"대체 재료: {row[5]}")
            print(f"조리 방법: {row[6]}")
            print(f"조리 시간: {row[7]}")
            print(f"난이도: {row[8]}")
            print(f"이미지 URL: {row[9]}")
            print(f"생성 날짜: {row[10]}")
            print("-" * 50)

        conn.close()

    except sqlite3.Error as e:
        print(f"DB 조회 오류: {e}")

# 테스트 실행
if __name__ == "__main__":
    fetch_all_recipes()
