from app import create_app
from app.database_setup import create_recipes_table

app = create_app()

if __name__ == "__main__":
    #DB 초기화
    create_recipes_table()

    #flask 앱 실행
    app.run(debug=True)

