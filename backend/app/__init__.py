from flask import Flask, render_template,request,jsonify
import requests

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    ROBOFLOW_API_KEY = "api_key"
    ROBOFLOW_MODEL_ID = "model_id"
    ROBOFLOW_VERSION_NUMBER = "1"
    ROBOFLOW_API_URL = ""

    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingres')
    def ingredients_search():
        return render_template('ingrespage.html')

    
    @app.route('/cooktip')
    def cooktip():
        return render_template('cooktip.html')
    
    @app.route('/camera')
    def camera():
        return render_template('search_camera.html')
    
    @app.route('/prdict', methods=['POST'])
    def predict():
        if 'file' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
    
        image_file = request.files['file']
        
        response = requests.post(
            ROBOFLOW_API_URL,
            files={"file": file}
        )

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Roboflow API 요청 실패", response.status_code }), 500

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


    return app
