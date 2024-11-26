# backend/app/auth/login/__init__.py
from flask import Blueprint

# 로그인 관련 블루프린트 정의 (auth_bp는 /auth/login 경로를 처리)
login_bp = Blueprint('login', __name__, url_prefix='/login')

# routes.py에 정의된 라우트들을 임포트
from app.auth.login import routes
