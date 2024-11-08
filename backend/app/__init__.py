from flask import Flask, render_template

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
    
    @app.route('/recipe_register')
    def recipe_register():
        return render_template('recipe_register.html')
    
    @app.route('/recipe_register2')
    def recipe_register2():
        return render_template('recipe_register2.html')


    return app
