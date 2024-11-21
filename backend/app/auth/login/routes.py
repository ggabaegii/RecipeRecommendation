from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.auth.login.forms import LoginForm, SignupForm
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.login.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 로그인 페이지
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 데이터베이스에서 이메일로 사용자 조회
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id  # 세션에 사용자 정보 저장
            return redirect(url_for('main.home'))  # 로그인 후 홈으로 리다이렉트
        flash('Invalid email or password')
    return render_template('login.html', form=form)

