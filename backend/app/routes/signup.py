from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import os
import sqlite3

# 블루프린트 정의
signup_bp = Blueprint('signup', __name__)

# 회원가입 라우트
@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            # 입력 데이터 수집
            profile_picture = request.files['profile-picture']
            nickname = request.form['nickname']
            real_name = request.form['real_name']
            gender = request.form.get('gender', '')
            birthdate = request.form['birthdate']
            phone_number = request.form['phone_number']
            email = request.form['email']
            username = request.form['username']
            password = generate_password_hash(request.form['password'])
            security_question_1 = request.form['security_question_1']
            security_answer_1 = request.form['security_answer_1']
            security_question_2 = request.form['security_question_2']
            security_answer_2 = request.form['security_answer_2']

            # 이미지 저장
            picture_path = None
            if profile_picture and profile_picture.filename:
                upload_folder = os.path.join('app/static/uploads')
                os.makedirs(upload_folder, exist_ok=True)
                picture_path = os.path.join(upload_folder, profile_picture.filename)
                profile_picture.save(picture_path)

            # 데이터베이스 저장
            conn = sqlite3.connect('app/database/users.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (profile_picture, nickname, real_name, gender, birthdate, phone_number, email, username, password, security_question_1, security_answer_1, security_question_2, security_answer_2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (picture_path, nickname, real_name, gender, birthdate, phone_number, email, username, password, security_question_1, security_answer_1, security_question_2, security_answer_2))
            conn.commit()
            conn.close()

            flash('회원가입이 성공적으로 완료되었습니다!')
            return redirect(url_for('login'))  # 로그인 페이지로 이동
        except Exception as e:
            flash(f'오류가 발생했습니다: {e}')
            return redirect(url_for('signup'))

    return render_template('signup.html')
