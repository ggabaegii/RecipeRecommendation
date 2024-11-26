from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import traceback

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'your_secret_key'  # 플래시 메시지용 비밀 키
    
    # API 키 및 URL 설정
    app.config["ROBOFLOW_API_KEY"] = "5dKfVfDaRwE3ueqLOz9s"
    app.config["ROBOFLOW_API_URL"] = "https://detect.roboflow.com/ingredients-detection-yolov8/2"

    # 임시 사용자 데이터 저장소
    users = []

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

    # 회원가입 라우트
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            # 사용자 데이터 수집
            user_data = {
                "nickname": request.form.get('nickname'),
                "name": request.form.get('name'),
                "gender": request.form.get('gender'),
                "birthdate": request.form.get('birthdate'),
                "phone": request.form.get('phone'),
                "email": request.form.get('email'),
                "username": request.form.get('username'),
                "password": request.form.get('password'),
                "security_question1": request.form.get('security_question1'),
                "answer1": request.form.get('answer1'),
                "security_question2": request.form.get('security_question2'),
                "answer2": request.form.get('answer2'),
            }

            # 비밀번호 확인
            if request.form.get('password') != request.form.get('confirm_password'):
                flash("비밀번호가 일치하지 않습니다.", "error")
                return render_template('signup.html')

            # 사용자 데이터 저장
            users.append(user_data)

            # 성공 시 로그인 페이지로 리다이렉트
            flash("회원가입이 완료되었습니다! 로그인하세요.", "success")
            return redirect(url_for('login'))

        return render_template('signup.html')

    return app
