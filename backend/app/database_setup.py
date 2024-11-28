from sqlalchemy import create_engine, Column, Integer, String, Enum, Date, TIMESTAMP, func, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# 기본 설정
Base = declarative_base()

class User(Base):
    __tablename__ = 'user' # 데이터베이스의 테이블 이름
    
    user_no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # user 데이터베이스 저장위한 부여 번호
    user_id = Column(String(50), nullable=False, unique=True)                        # user ID
    user_name = Column(String(50), nullable=False, unique=True)                      # user 이름
    hashed_pw = Column(String(255), nullable=False)                                  # 해시된 비밀번호
    user_gender = Column(Enum('MALE', 'FEMALE'), nullable=False)                     # 성별
    user_birthday = Column(Date, nullable=True)                                      # 생년월일
    user_phone = Column(String(25), nullable=True)                                   # 휴대폰 번호
    hint_question_1 = Column(String(255), nullable=True)                             # 비밀번호 힌트 질문1번
    hint_answer_1 = Column(String(255), nullable=True)                               # 비밀번호 힌트 질문1번 답변
    hint_question_2 = Column(String(255), nullable=True)                             # 비밀번호 힌트 질문2번 
    hint_answer_2 = Column(String(255), nullable=True)                               # 비밀번호 힌트 질문2번 답변
    user_email = Column(VARCHAR(100), nullable=False, unique=True)                   # user 이메일
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())               # 계정 생성 날짜
    updated_at = Column(TIMESTAMP, nullable=True, onupdate=func.now())               # 계정 업데이트 날짜
    profile_image = Column(String(255), nullable=True, default='/static/images/profiles/default-profile.png') # user 프로필 이미지

# SQLite 데이터베이스 생성
def setup_database():
    engine = create_engine('sqlite:///app.db')     # 데이터베이스 엔진 생성
    Base.metadata.create_all(engine)                # 테이블 생성
    print("Database and tables created successfully.")

if __name__ == "__main__":
    setup_database()