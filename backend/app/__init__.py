from flask import Flask, render_template,request,jsonify
import requests
from .api import predict_from_image, get_recipes_from_gemini
from .database_operations import insert_recipes_to_db
import traceback
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

ROBOFLOW_API_URL = os.getenv("roboflow_API_URL")
ROBOFLOW_API_KEY = os.getenv("roboflow_API_KEY")


def create_app():
    app = Flask(__name__, template_folder='templates')
    
    def fetch_all_recipes():
        conn = sqlite3.connect("C:/RecipeRecommendation/backend/app/database.db")  # DB 파일 이름
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes")  # 레시피 이름과 이미지 경로 가져오기
        recipes = cursor.fetchall()  # [(name1, image_path1), (name2, image_path2), ...]
        conn.close()
        return recipes
   
    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingr_sea')
    def ingredients_search():
        # DB에서 레시피 데이터를 가져옴
        recipes = fetch_all_recipes()
        # ingredients = predict() ##선택된 재료 보여주려면 yolo로 받아온 ingredients 받아와야됨 어떻게??
        # 이름만 추출하여 템플릿에 전달
        recipe_names = [recipe[1] for recipe in recipes]  # recipe[1]은 이름
        recipe_descriptions = [recipe[3] for recipe in recipes]
        recipe_ids = [recipe[0] for recipe in recipes]
        return render_template("ingrespage.html", recipe_names=recipe_names, recipe_descriptions=recipe_descriptions, recipe_ids=recipe_ids)
           
    
    
    @app.route('/cooktip')
    def cooktip():
        return render_template('cooktip.html')
    

    @app.route('/cooktip_detail')
    def cooktip_detail():
        return render_template('cooktip_detail.html')
    

    @app.route('/search_camera')
    def camera():
        return render_template('search_camera.html')
                    
    @app.route('/prdict', methods=['POST'])
    def predict():
        if 'file' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['file']

        try:
            # API 호출 함수
            yolo_result = predict_from_image(
                file,
                ROBOFLOW_API_URL,
                ROBOFLOW_API_KEY
            )
            ingredients = yolo_result.get('ingredients', [])

            recipes_data = get_recipes_from_gemini(ingredients)
            print("recipes_data 타입:",type(recipes_data))
            print("recipes_data 내용:", recipes_data)
             
            recipes = recipes_data.get('gemini_answer', {}).get('recipes', [])

            if recipes:
                insert_recipes_to_db(recipes)


            return jsonify({'recipes': recipes})
        
        except Exception as e:
            print("Error occurred:", traceback.format_exc())
            return jsonify({'error': str(e)}), 500
        

    @app.route('/locspepage')
    def locspepage():
        return render_template('locspepage.html')
    


    @app.route('/mypagemain')
    def mypagemain():
        return render_template('mypagemain.html')
    
    @app.route('/mypagesub')
    def mypagesub():
        return render_template('mypagesub.html')
    
    # 상세 페이지 라우트
    @app.route("/recipe_detail/<int:recipe_id>")
    def recipe_detail(recipe_id):
        conn = sqlite3.connect("C:/RecipeRecommendation/backend/app/database.db")  # DB 파일 이름
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id,))
        recipe = cursor.fetchone()
        conn.close()

        if recipe:
            return render_template("recipe_detail.html", name=recipe[1], category = recipe[2], description=recipe[3], cook_time = recipe[7], difficulty=recipe[8])
        else:
            return "Recipe not found", 404
    
    # @app.route('/recipe_detail')
    # def recipe_detail():
    #     return render_template('recipe_detail.html')

    @app.route('/recipe_main')
    def recipe_main():
        return render_template('recipe_main.html')
    

    @app.route('/recipe_register')
    def recipe_register():
        return render_template('recipe_register.html')


    @app.route('/recipe_search')
    def recipe_search():
        return render_template('recipe_search.html')

    @app.route('/searecpage')
    def searecpage():
        return render_template('searecpage.html')

    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    # 사용자 정보 수정
    @app.route('/userinfo_edit', methods=['GET', 'POST'])
    def userinfo_edit():
        return render_template('userinfo_edit.html')

    return app
