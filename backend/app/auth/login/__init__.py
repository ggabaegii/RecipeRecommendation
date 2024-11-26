# app/auth/login/__init__.py
from flask import Blueprint, render_template, request, redirect, url_for

# Blueprint 생성
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 로그인 페이지 라우트
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')  # 로그인 페이지로 렌더링

# 회원가입 페이지 라우트
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')  # 회원가입 페이지로 렌더링
