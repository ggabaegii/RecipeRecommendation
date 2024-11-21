from flask import Flask, render_template,request,jsonify
import requests
#from inference_sdk import InferenceHTTPClient
from .api import predict_from_image
import traceback

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    app.config["ROBOFLOW_API_KEY"] = "5dKfVfDaRwE3ueqLOz9s"
    app.config["ROBOFLOW_API_URL"] = "https://detect.roboflow.com/ingredients-detection-yolov8/2"

    
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
            result = predict_from_image(
                file,
                app.config['ROBOFLOW_API_URL'],
                app.config['ROBOFLOW_API_KEY']
            )
            return jsonify(result)
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

    return app
