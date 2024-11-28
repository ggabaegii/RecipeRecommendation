import base64
import requests
import google.generativeai as genai
import json
import os
import re
from dotenv import load_dotenv

# 숫자-재료 매핑
MATERIAL_MAPPING = {
    '1': "소고기", '2': "양배추", '3': "당근", '4': "닭고기", '5': "고추",
    '7': "오이", '8': "달걀", '9': "생선", '10': "마늘",
    '11 0 0 0 1 1 1 1 0 0 0' : "사과",
    '11': "생강", '13': "레몬", '14': "라임", '15': "우유",
    '16': "버섯", '17': "면", '18': "양파", '19': "오렌지",
    '21': "땅콩", '22': "돼지고기", '23': "감자", '24': "새우", '25': "밥",
    '26': "대파", '28': "토마토"
}

def map_class_to_material(class_id):
    return MATERIAL_MAPPING.get(class_id, "알 수 없음")

def predict_from_image(image_file, api_url, api_key):
    """
    Roboflow API를 호출하여 이미지에서 재료를 예측합니다.
    :param image_file: 업로드된 이미지 파일
    :param api_url: Roboflow API URL
    :param api_key: Roboflow API Key
    :return: 예측된 재료 리스트
    """
    # 이미지를 base64로 인코딩
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    
    try: # API 호출
        response = requests.post(
            api_url,
            params={"api_key": api_key},
            data=encoded_image,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        # 응답 확인 및 결과 반환
        response.raise_for_status()
        data = response.json()
        print("Roboflow Response:", data)

        #응답 데이터 확인
        if "predictions" not in data:
            raise ValueError("API 응답에 'predictions' 필드가 없습니다.")
        
        #예측 결과 확인
        predictions = data.get("predictions", [])
        ingredients = list({
            map_class_to_material((pred["class"]))  # 클래스 ID를 재료 이름으로 변환
            for pred in predictions if pred.get("confidence", 0) > 0.5  # 신뢰도 50% 이상만 사용
        })
        
        print(ingredients)

        if not ingredients:
            raise ValueError("재료를 인식하지 못했습니다.")


        return {"ingredients": ingredients}
   

    except ValueError as ve:
        print("Value Error:", ve)
        raise
    except requests.exceptions.RequestException as re:
        print("Request Error:", re)
        raise
    except Exception as e:
        print("Unexpected Error:", e)
        raise


#제미나이 API
############################################
load_dotenv()
google_api_key = os.getenv("genai_api_key")
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction="""
        You are Korean. You are a chef. Please respond with structured JSON data.                    
    """
    )

def get_recipes_from_gemini(ingredients):
    '''
    제미나이 API를 호출하여 재료로 만들 수 있는 레시피를 JSON형식으로 추천받는다.
    :param ingredients: YOLO 모델에서 검출된 재료 리스트
    :return: 추천받은 레시피 데이터 (JSON 형태)
    ''' 
    prompt = f"""
    아래 재료를 활용하여 3개의 요리 레시피를 추천해 주세요
    {', '.join(ingredients)}

    각 레시피는 다음 정보를 포함해야 합니다.
    1. 레시피 번호
    2. 요리 이름
    3. 한식, 양식, 중식 등의 카테고리
    4. 요리에 대한 간단한 설명
    5. 필요한 재료 목록
    6. 대체 가능한 재료 목록
    7. 조리 방법 (단계별 설명)
    8. 조리 시간
    9. 요리 난이도 ( 쉬움, 보통, 어려움 중 하나)
    10. 요리 이미지 URL
    """

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                temperature=1.0,
                response_mime_type="application/json"
            )
        )
        
        try:
            # JSON 응답 파싱
            change_response = json.loads(response.text)
            print("JSON 데이터 타입:", type(change_response))

            response_data={
                "message": "성공",
                "gemini_answer":change_response
            }
            print("응답 데이터:", response_data)

            return response_data  # 결과 반환
            
        except json.JSONDecodeError as e:
            print("JSON 파싱 실패:", e)

    except json.JSONDecodeError:
        print("OpenAI 응답 JSON 파싱 실패.")
        raise Exception("Gemini 응답 파싱 실패")
    except Exception as e:
        print(f"Gemini API 호출 중 오류 발생: {e}")
        raise