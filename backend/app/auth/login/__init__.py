from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite 데이터베이스 파일 경로
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key'  # 세션 사용을 위한 시크릿 키 설정

    db.init_app(app)
    Migrate(app, db)  # 데이터베이스 마이그레이션 초기화

    # Blueprint 등록
    from app.auth.login import auth_bp
    app.register_blueprint(auth_bp)

    return app
