from flask import Flask, render_template,request,jsonify

def create_app():
    app = Flask(__name__, template_folder='templates')
    #app.secret_key = 'your_secret_key'

    # 라우트 정의
    @app.route('/')
    def home():
        return render_template('mainpage.html')

    @app.route('/ingres')
    def ingredients_search():
        return render_template('ingrespage.html')

    @app.route('/camera')
    def camera():
        return render_template('camera.html')
    
    @app.route('/cooktip')
    def cooktip():
        return render_template('cooktip.html')
    
    
    @app.route('/process_image', methods=['POST'])
    def process_image():
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
    
        image_file = request.files['image']
        #ingredients = detect_ingredients(image_file)  # YOLO 모델로 재료 인식
    
        #return jsonify({'ingredients': ingredients})

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
