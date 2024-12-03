# backend/app/auth/__init__.py
from flask import Blueprint

# Blueprint 정의 (auth_bp는 /auth 경로를 처리)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# login 폴더 내의 라우트 파일 임포트
from app.auth.login import routes