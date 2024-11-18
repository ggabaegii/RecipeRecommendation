from flask import Flask, render_template,request,jsonify
import requests
from inference_sdk import InferenceHTTPClient

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    ROBOFLOW_API_KEY = "5dKfVfDaRwE3ueqLOz9s"
    MODEL_ID = "ingredients-detection-yolov8/2"
    API_URL = "https://detect.roboflow.com"

    # Roboflow Inference Client 설정
    client = InferenceHTTPClient(api_url=API_URL, api_key=ROBOFLOW_API_KEY)

    #app.secret_key = 'your_secret_key'
    
    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingr_sea')
    def ingredients_search():
        return render_template('ingrespage.html')
        #ingredients = request.args.get("ingredients", "").split(',')
        #excluded = request.args.get("excluded", "").split(',')
    
    # DB에서 ingredients와 관련된 레시피를 검색하는 로직 추가 필요
    # 예시: 레시피 목록 조회
        #recipes = search_recipes_by_ingredients(ingredients, excluded)
    
        #return render_template("ingrespage.html", recipes=recipes)


    
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
            # Roboflow API로 이미지 예측
            result = client.infer(file, model_id=MODEL_ID)
            predictions = result.get("predictions", [])
            
            # 예측 결과에서 클래스 이름만 추출하여 반환
            ingredients = [pred["class"] for pred in predictions]
            return jsonify({"ingredients": ingredients})
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        

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



    def search_recipes_by_ingredients(ingredients, excluded):
    # DB 연결 및 검색 로직 예시 (실제 구현 시 DB 쿼리 필요)
    # 이 함수는 DB에서 재료와 관련된 레시피를 조회하는 역할을 합니다.
        dummy_recipes = [
            {"title": "토마토 스파게티", "ingredients": ["토마토", "스파게티"]},
            {"title": "감자 샐러드", "ingredients": ["감자", "마요네즈"]},
            {"title": "버섯 리조또", "ingredients": ["버섯", "쌀"]},
        ]
        # 테스트 목적의 더미 데이터 사용
    
        return [recipe for recipe in dummy_recipes if any(ing in recipe["ingredients"] for ing in ingredients) and not any(excl in recipe["ingredients"] for excl in excluded)]

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

    return app
