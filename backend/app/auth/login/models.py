# app/auth/login/models.py

from app.db import db  # db 객체를 app.db에서 가져옵니다.

class User(db.Model):
    __tablename__ = 'users'  # 테이블 이름 설정

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # 기타 필드와 메서드를 추가할 수 있습니다.
