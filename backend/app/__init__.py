from flask import Flask, render_template,request,jsonify
import requests
# from inference_sdk import InferenceHTTPClient

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    ROBOFLOW_API_KEY = "5dKfVfDaRwE3ueqLOz9s"
    ROBOFLOW_MODEL_ID = "ingredients-detection-yolov8/2"
    ROBOFLOW_VERSION_NUMBER = "2"
    ROBOFLOW_API_URL = "https://detect.roboflow.com"

    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingres')
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
    
    @app.route('/search_camera')
    def camera():
        return render_template('search_camera.html')
    
    @app.route('/prdict', methods=['POST'])
    def predict():
        # 아래 코드는 추후 삭제
        data = request.json
        ingredients = data.get("ingredients", [])

        # 테스트 코드
        response = {
            "message" : "인식된 재료가 성공적으로 전달되었습니다.",
            "ingredients" : ingredients
        }
        return jsonify(response)
    

        if 'file' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
    
        image_file = request.files['file']
        
        response = requests.post(
            ROBOFLOW_API_URL,
            files={"file": image_file}
        )

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Roboflow API 요청 실패", "status_code": response.status_code }), 500

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

    
    @app.route('/recipe_register')
    def recipe_register():
        return render_template('recipe_register.html')
    
    @app.route('/recipe_register2')
    def recipe_register2():
        return render_template('recipe_register2.html')


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


    return app
