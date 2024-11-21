from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# 로그인 폼
class LoginForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired()])  # 아이디 필드
    password = PasswordField('비밀번호', validators=[DataRequired()])  # 비밀번호 필드
    submit = SubmitField('로그인')

