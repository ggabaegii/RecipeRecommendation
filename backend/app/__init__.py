from flask import Flask, render_template,request,jsonify
import requests
from .api import predict_from_image, get_recipes_from_gemini
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

ROBOFLOW_API_URL = os.getenv("roboflow_API_URL")
ROBOFLOW_API_KEY = os.getenv("roboflow_API_KEY")


def create_app():
    app = Flask(__name__, template_folder='templates')
    

   
    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingr_sea')
    def ingredients_search():
        return render_template('ingrespage.html')
    
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

            recipes = get_recipes_from_gemini(ingredients)

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
    
    @app.route('/recipe_detail')
    def recipe_detail():
        return render_template('recipe_detail.html')

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
