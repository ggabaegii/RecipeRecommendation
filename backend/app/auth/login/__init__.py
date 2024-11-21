# app/auth/login/__init__.py
from flask import Blueprint

# 로그인 관련 Blueprint 등록
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import routes  # routes.py의 routes들을 import
