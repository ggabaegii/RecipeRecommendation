from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User

# 데이터베이스 연결 설정
engine = create_engine('sqlite:///app.db') # 데이터베이스 엔진 생성
Session = sessionmaker(bind=engine)
session = Session()

# 회원 가입 함수
def add_user(user_id, user_name, hashed_pw, user_gender, user_birthday=None, 
             user_phone=None, hint_question_1=None, hint_answer_1=None,
             hint_question_2=None, hint_answer_2=None, user_email=None, profile_image=None):
    try:
        new_user = User(
            user_id=user_id,
            user_name=user_name,
            hashed_pw=hashed_pw,
            user_gender=user_gender,
            user_birthday=user_birthday,
            user_phone=user_phone,
            hint_question_1=hint_question_1,
            hint_answer_1=hint_answer_1,
            hint_question_2=hint_question_2,
            hint_answer_2=hint_answer_2,
            user_email=user_email,
            profile_image=profile_image
        )
        session.add(new_user)
        session.commit()
        print("User added successfully!")
    except Exception as e:
        session.rollback()
        print("Error adding user:", e)

# 모든 사용자 출력 함수
def get_all_users():
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        print("Error retrieving users:", e)
        return []
    
# 회원 정보 수정 함수
def update_user(user_id, **kwargs):
    """
    회원 정보를 수정하는 함수.

    :param user_id: 수정하려는 사용자의 ID
    :param kwargs: 수정하려는 필드와 값 (예: user_name="새 이름", user_email="새 이메일")
    """
    try:
        # 사용자 검색
        user = session.query(User).filter(User.user_id == user_id).first()
        
        if not user:
            print(f"User with ID '{user_id}' not found.")
            return False
        
        # 전달된 필드를 동적으로 업데이트
        for key, value in kwargs.items():
            if hasattr(user, key):  # User 모델에 해당 필드가 있는지 확인
                setattr(user, key, value)
            else:
                print(f"Invalid field: {key}. Skipping.")
        
        session.commit()
        print(f"User with ID '{user_id}' updated successfully!")
        return True
    except Exception as e:
        session.rollback()
        print("Error updating user:", e)
        return False

# 회원 삭제 함수
def delete_user(user_id):
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print("User deleted successfully!")
        else:
            print("User not found.")
    except Exception as e:
        session.rollback()
        print("Error deleting user:", e)

if __name__ == "__main__":
    # 테스트 예제
    add_user(
        user_id="testuser",
        user_name="John Doe",
        hashed_pw="hashedpassword123",
        user_gender="MALE",
        user_email="john.doe@example.com"
    )
    
    # 사용자 정보 업데이트 테스트
    result = update_user(
        "testuser", 
        user_name="Updated Name", 
        user_email="updated_email@example.com",
        user_phone="010-1234-5678"
    )
    
    if result:
        print("User updated successfully!")
    else:
        print("Failed to update user.")

    users = get_all_users()
    for user in users:
        print(f"ID: {user.user_id}, Name: {user.user_name}, Email: {user.user_email}")
