from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL  # flask_mysqldb로 수정
from app.auth.login.routes import auth_bp  # auth 블루프린트를 가져옵니다

# MySQL 객체 초기화
mysql = MySQL()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # MySQL 연결 설정
    app.config['MYSQL_HOST'] = 'localhost'  # MySQL 서버 주소
    app.config['MYSQL_USER'] = 'root'  # MySQL 사용자
    app.config['MYSQL_PASSWORD'] = 'your_mysql_password'  # MySQL 비밀번호
    app.config['MYSQL_DB'] = 'your_database_name'  # 사용할 데이터베이스 이름

    # MySQL 객체와 Flask 앱 연결
    mysql.init_app(app)

    # 비밀 키 설정
    app.config['SECRET_KEY'] = 'your_secret_key'  # 세션을 위한 비밀 키 설정

    # 블루프린트를 '/auth' 접두어와 함께 등록
    app.register_blueprint(auth_bp, url_prefix='/auth')

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
