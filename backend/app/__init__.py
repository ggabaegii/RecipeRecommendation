from flask import Flask, render_template,request,jsonify

def create_app():
    app = Flask(__name__, template_folder='templates')
    #app.secret_key = 'your_secret_key'

    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('main.html')

    @app.route('/recipe_search')
    def recipe_search():
        return render_template('recipe_search.html')

    @app.route('/camera')
    def camera():
        return render_template('camera.html')
    
    @app.route('/cooktip')
    def cookingtips():
        return render_template('cooktip.html')
    
    @app.route('/recipesearch')
    def recopesearch():
        return render_template('recipe_search.html')
    
    @app.route('/process_image', methods=['POST'])
    def process_image():
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
    
        image_file = request.files['image']
        #ingredients = detect_ingredients(image_file)  # YOLO 모델로 재료 인식
    
        #return jsonify({'ingredients': ingredients})

    return app
