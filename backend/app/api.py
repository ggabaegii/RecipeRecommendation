import base64
import requests

# 숫자-재료 매핑
MATERIAL_MAPPING = {
    1: "소고기", 2: "양배추", 3: "당근", 4: "닭고기", 5: "고추",
    6: "검출 무시", 7: "오이", 8: "달걀", 9: "생선", 10: "마늘",
    11: "생강", 12: "검출 무시", 13: "레몬", 14: "라임", 15: "우유",
    16: "버섯", 17: "면", 18: "양파", 19: "오렌지", 20: "검출 무시",
    21: "땅콩", 22: "돼지고기", 23: "감자", 24: "새우", 25: "밥",
    26: "대파", 27: "검출 무시", 28: "토마토", 29: "검출 무시"
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
        predictions = data.get("predictions", [])
        ingredients = [pred["class"] for pred in predictions]


        #응답 데이터 확인
        if "predictions" not in data:
            raise ValueError("API 응답에 'predictions' 필드가 없습니다.")
        
        #예측 결과 확인
        predictions = data.get("predictions", [])
        ingredients = [
            map_class_to_material((pred["class"]))  # 클래스 ID를 재료 이름으로 변환
            for pred in predictions if pred.get("confidence", 0) > 0.5  # 신뢰도 50% 이상만 사용
        ]

        print(ingredients)
        print(pred)
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