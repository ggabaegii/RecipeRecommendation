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
    
    @app.route('/mypagemain')
    def mypagemain():
        return render_template('mypagemain.html')
    
    @app.route('/mypagesub')
    def mypagesub():
        return render_template('mypagesub.html')

    return app
