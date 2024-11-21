from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.auth.signup.forms import SignupForm
from app import db
from werkzeug.security import generate_password_hash
from app.auth.signup.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 회원가입 페이지
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # 이메일 중복 확인
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('이미 사용 중인 이메일입니다.', 'danger')
            return redirect(url_for('auth.signup'))

        # 비밀번호 확인
        if form.password.data != form.confirm_password.data:
            flash('비밀번호가 일치하지 않습니다.', 'danger')
            return redirect(url_for('auth.signup'))

        # 비밀번호 해시화
        hashed_password = generate_password_hash(form.password.data)
        
        # 새로운 사용자 생성하여 데이터베이스에 저장
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()  # DB에 저장

        flash('Your account has been created!', 'success')
        return redirect(url_for('auth.login'))  # 회원가입 후 로그인 페이지로 리다이렉트

    return render_template('signup.html', form=form)
