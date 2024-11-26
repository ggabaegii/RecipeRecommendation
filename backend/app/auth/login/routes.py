from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.auth.login.forms import LoginForm
from app.auth.login.models import User
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 로그인 페이지
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 데이터베이스에서 아이디로 사용자 조회
        user = User.query.filter_by(username=form.username.data).first()  # 아이디로 사용자 조회
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id  # 세션에 사용자 정보 저장
            flash('로그인 성공!', 'success')  # 로그인 성공 메시지
            return redirect(url_for('main.home'))  # 로그인 후 홈으로 리다이렉트
        else:
            flash('잘못된 아이디 또는 비밀번호입니다.', 'danger')  # 실패 메시지
    return render_template('login.html', form=form)
