from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.auth import auth_bp

# SQLAlchemy 객체 초기화
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # MySQL 연결 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:your_mysql_password@localhost/your_database_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # SQLAlchemy의 변경 추적 비활성화
    app.config['SECRET_KEY'] = 'your_secret_key'  # 세션을 위한 비밀 키 설정

    # db 객체와 Flask 앱 연결
    db.init_app(app)

    # 블루프린트를 '/auth' 접두어와 함께 등록
    app.register_blueprint(auth_bp)

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
    
    @app.route('/recipe_list')
    def recipe_list():
        return render_template('recipe_list.html')

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
